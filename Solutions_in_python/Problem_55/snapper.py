#!/usr/bin/env python

import os
import sys
import copy

folder = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(folder, 'C-small-attempt0.in')
file = open(filepath, 'r')

i = 0
j = 0
groups = []
data = []
cases = []
for line in file:
    if i == 0:
        i = int(line.rstrip())
    else:
        if j > 1:
            j = 0
        if j == 0:
            data = line.rstrip().split(' ')
            for m in xrange(len(data)):
                data[m] = int(data[m])   
            j = j+1
        elif j == 1:
            groups = line.rstrip().split(' ')
            for m in xrange(len(groups)):
                groups[m] = int(groups[m])            
            j = j+1
    if j > 1:
        cases.append([data, groups])
file.close()

br = 1
for case in cases:
    R = case[0][0]
    k = case[0][1]
    N = case[0][2]
    price = 0
    lista = copy.deepcopy(case[1])
    for i in xrange(R):
        roller = []
        for j in xrange(len(case[1])):
            br1 = copy.deepcopy(lista[0])
            if sum(roller)+br1 <= k:
                roller.append(br1)
                lista.pop(0)
                lista.append(br1)
        price = price + sum(roller)
    print "Case #"+str(br)+": "+str(price)
    br += 1