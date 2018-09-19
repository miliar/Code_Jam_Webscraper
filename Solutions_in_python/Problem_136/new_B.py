# -*- coding: utf-8 -*-

f = open("B-small-attempt24.in")
#f = open("test.txt")
testCaseNumber = int(f.readline())




final_text = ""



def buy_n_time(C, F, X, time):
    # C mean how many cookies can buy a farm.
    # F mean after buy a farm, extra F cookies per second.
    # X mean cookies number goal.

    cookies_rate = 2
    # how many cookies per second
        
    if time == 0:
        return X / cookies_rate

    total_buy_time = 0
    for t in list(range(0, time)):
        buy_time = C / cookies_rate
        cookies_rate = cookies_rate + F
        total_buy_time = total_buy_time + buy_time
                
    wait_time = X / cookies_rate

    result = wait_time + total_buy_time
    return result









for case_number in list(range(1, testCaseNumber+1)):
    one_case = f.readline()
    one_case_list = one_case.split()
    C = float(one_case_list[0])
    F = float(one_case_list[1])
    X = float(one_case_list[2])
    # C mean how many cookies can buy a farm.
    # F mean after buy a farm, extra F cookies per second.
    # X mean cookies number goal.    

    
    l = []

    

    
    

    #print("C:" + str(C) + " F: " + str(F) + " X: " + str(X) )
    #print(str(type(C)))
    #break


    #######################################
    #
    #  3个数字我们现在拿到了, 现在开始计算~
    #
    #######################################

    
    # 买不同次数的 farm 后会如何?
    # 我只买1次farm, 然后干等到goal呢?  我只买2次farm, 然后干等到goal呢?  我只买3.............
    time_list = []
    '''
    for time in list(range(0,999)):
        t = buy_n_time(C, F, X, time)
        #t = buy_n_time(500.0, 4.0, 2000.0, time)
        
        if len(time_list) > 1 and float(t) > float(time_list[-1]):
            break
        time_list.append(t)
    
    '''

    
    timeaaaa = 0
    while True:
        t = buy_n_time(C, F, X, timeaaaa)
        if len(time_list) > 1 and float(t) > float(time_list[-1]):
            break
        else:
            time_list.append(t)
        timeaaaa = timeaaaa + 1

    r = min(time_list)
    r = round(r, 7)
    r = "{:.7f}".format(r)

    
    # 输出最终结果
    case = "Case #" + str(case_number) + ": " + str(r)
    final_text = final_text + case + "\n"
    
    



print(final_text)



# 输出到文件里
with open('new_B_out.txt', 'w') as file:
    file.write(final_text)



