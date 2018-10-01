#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def inv(robot):
    if robot == "B":
        return "O"
    return "B"

f = open(sys.argv[1])
nb_case = int(f.readline())
for i in range(nb_case):
    order = f.readline().split(" ")
    nb_command = int(order[0])
    cumul = {"O": 0, "B": 0}
    last_case = {"O": 1, "B": 1}
    response = 0
    for j in range(1, (2*nb_command)+1, 2):
        me = order[j]
        nb_sec = abs(last_case[me] - int(order[j+1])) + 1
        if nb_sec - cumul[me] <= 0 :
            nb_sec = 1
        else:
            nb_sec -= cumul[me]
        cumul[inv(me)] += nb_sec
        cumul[me] = 0
        response += nb_sec
        last_case[me] = int(order[j+1])
    print("Case #" + str(i+1) + ": " + str(response))
    
