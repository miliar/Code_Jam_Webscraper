#!/usr/bin/env python
#-*- coding:utf-8 -*-

def check_combination(result,combination,new_element):
    if result == []:
        return False,0

    last_element = result[len(result)-1]
    
    if last_element != new_element:
        for i in combination:
            if (new_element in i) and (last_element in i):
                return True,i[2]
    else:
        for i in combination:
            if (new_element+last_element in i):
                return True,i[2]
        
    return False,0
    
def check_opposite(result,opposite,new_element):
    if result == []:
        return False

            
    for i in opposite:
        for j in result:
            if (new_element in i) and (j in i) and (new_element != j):
                return  True
                
    return False
    

inp = open("input2.txt","r")
outp = open("output_large.txt","w")

lines = inp.readline()
lines = lines.split()
lines = int(lines[0])

for i in range (0,lines):
    outp.write ("Case #" + str(i+1) + ": ")

    test = inp.readline()
    test = test.split()

    #Set combinations list
    ncomb = int(test[0])
    combination_list = []
    for i in range (0,ncomb):
        combination_list.append(test[i+1])
        
    #Set opposites lists
    nopp = int(test[ncomb+1])
    opposite_list = []
    for i in range(ncomb+2,nopp+ncomb+2):
        opposite_list.append(test[i])
            
    ninvokes = int(test[ncomb+nopp+2])
    invoke_list = test[ncomb+nopp+3]
    
    result_list = [invoke_list[0]]
    aux_counter = 0
    for i in range(1,ninvokes):
        if aux_counter == 0:
            flag,new = check_combination(result_list, combination_list, invoke_list[i])
        else:
            flag = False
            aux_counter = 0
                
        flag_opp = False            
        if not flag:
            flag_opp = check_opposite(result_list,opposite_list, invoke_list[i])
        else:
            result_list.pop()
            result_list.append(new)
            aux_counter = 1
            continue
            
        if flag_opp:
            result_list = []
        else:
            result_list.append(invoke_list[i])
   
    outp.write ("[")
    for i in range (0,len(result_list)-1):
        outp.write(result_list[i] + ", ")
        
    if result_list != []:
        outp.write(result_list[len(result_list)-1] + "]\n")
    else:
        outp.write("]\n")

inp.close()
outp.close()
