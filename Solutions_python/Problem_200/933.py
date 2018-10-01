# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 18:23:26 2017

@author: Trevor
"""

def last_tidynum(num_str):
    if len(num_str) == 1:
        return num_str
    if num_str[0] < num_str[1]:
        return num_str[0] + last_tidynum(num_str[1:])
    elif num_str[0] == num_str[1]:
        new_answer = last_tidynum(num_str[1:])
        if num_str[0] == new_answer[0]:
            return num_str[0] + new_answer
        else:
            if new_answer[0] == '0':
                return str(int(num_str[0])-1) + '9' + new_answer[1:]
            else:
                return str(int(num_str[0])-1) + '9' * (len(num_str)-1)
    else:
        return (str(int(num_str[0])-1)) + '9' * (len(num_str)-1)

def run(filename):
    f = open(filename,"r")
    data = f.read()
    f.close()
    inputs = data.splitlines()[1:]
    count = 1
    answer = ""
    for line in inputs:
        answer = answer + "Case #" + str(count)+": " + str(int(last_tidynum(line))) + "\n"
        count = count + 1
    f = open("OutputB","w")
    f.write(answer)
    f.close()