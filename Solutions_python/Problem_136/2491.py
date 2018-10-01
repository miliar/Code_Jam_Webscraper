import sys
import os

ifd = open("small.in", "r")
ofd = open("out.txt", "w")  
no_of_testcase = int(ifd.readline())
item_map = {} 
for i in range(no_of_testcase) :
    testcase_detail_str = ifd.readline() ; 
    testcase_detail_arr = testcase_detail_str.split() 
    cost_of_factory = float(testcase_detail_arr[0]) 
    extra_cookie = float(testcase_detail_arr[1]) 
    target = float(testcase_detail_arr[2])

    time = 0.0
    rate = 2.0
    run_simulation = 1
    while run_simulation == 1 :
        time_to_reach_target_without_factory = target / rate 
        time_to_buy_next_factory = cost_of_factory / rate 
        time_to_reach_target_with_factory = target / (rate + extra_cookie)
        if(time_to_reach_target_without_factory > (time_to_buy_next_factory + time_to_reach_target_with_factory)) : 
            time = time + time_to_buy_next_factory 
            rate = rate +  extra_cookie 
        else :
            time = time + (target / rate) 
            run_simulation = 0 
    ofd.write("Case #"+ str(i+1) + ": " + str(time) + "\n")
ifd.close()
ofd.close()


