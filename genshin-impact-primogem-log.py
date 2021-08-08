import time
from selenium import webdriver
def wheel_element(element, deltaY = 120, offsetX = 0, offsetY = 0): #this function is for internet
    error = element._parent.execute_script("""
        var element = arguments[0];
        var deltaY = arguments[1];
        var box = element.getBoundingClientRect();
        var clientX = box.left + (arguments[2] || box.width / 2);
        var clientY = box.top + (arguments[3] || box.height / 2);
        var target = element.ownerDocument.elementFromPoint(clientX, clientY);

        for (var e = target; e; e = e.parentElement) {
            if (e === element) {
            target.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
            return;
            }
        }    
        return "Element is not interactable";
        """, element, deltaY, offsetX, offsetY)
    if error:
        raise WebDriverException(error)
#download chromedriver form https://chromedriver.chromium.org/
chromedriver_path = 'D:\\chromedriver.exe'
driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
driver.set_window_position(0, 0)
driver.set_window_size(720, 1080)
#你的意見回饋網址(Feedback URL)
Feedback_URL = 'https://webstatic-sea.mihoyo.com/ys/event/im-service/...'
driver.get(Feedback_URL)
time.sleep(3)
driver.find_elements_by_xpath('//*[@id="J_classify-scroll"]/div/div[1]/div[2]')[0].click() #遊戲問題(In-game issue)
time.sleep(3)
driver.find_elements_by_xpath('//*[@id="J_contact_container"]/div[2]/div/div[2]/div[1]/p')[0].click() #自助查詢(Check Records)
time.sleep(3)
# driver.find_elements_by_xpath('//*[@id="J_contact_container"]/div[4]/div[1]/p/a[1]')[0].click() #創世結晶(Genesis Crystal)
driver.find_elements_by_xpath('//*[@id="J_contact_container"]/div[4]/div[1]/p/a[2]')[0].click() #原石(Primogem)
status = True
time.sleep(3)
# element = driver.find_element_by_css_selector("#scene > div.widget-scene > canvas")
element = driver.find_elements_by_xpath('/html/body/div[1]/div[2]')[0]
data = driver.find_elements_by_class_name('item-row')
data_size = 0
no_change_cnt = 0
data = []
while no_change_cnt < 5:
    for i in range(20):
        wheel_element(element, 8000)
        time.sleep(0.5)
    data = driver.find_elements_by_class_name('item-row')
    #time.sleep(1)
    
    if data_size == len(data):
        no_change_cnt+=1
    else:
        data_size = len(data)
        print("read: "+ str(int(data_size/4)))
        no_change_cnt = 0
print('start write file')
f = open("result.csv", mode='w',encoding='utf-8') # write data to csv file
cnt = 0
for i in range(len(data)):
    value = data[i].find_elements_by_class_name('item-text')
    f.write(value[0].get_attribute("innerText")+',')
    cnt += 1
    if cnt == 4:
        f.write("\n")
        cnt = 0
f.close()

