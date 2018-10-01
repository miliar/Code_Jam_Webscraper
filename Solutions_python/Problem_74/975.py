#!/usr/bin/python

import re
file = open('A-large-0.in')
output = open('A-large-0.out', 'w')
T = int(file.readline())

for i in range(1,T+1):
    current = re.findall('[BO] \d*', file.readline())
    
    lastOplace = 1
    lastBplace = 1
    lastOtime = 0
    lastBtime = 0
    curtime = 1
    for button in current:
        if button[0] == 'O':
            lastOtime+=abs(int(button[2:])-lastOplace)+1
            if(lastOtime<=lastBtime):
                lastOtime = lastBtime+1
            lastOplace = int(button[2:])
        else:
            lastBtime+=abs(int(button[2:])-lastBplace)+1
            if(lastBtime<=lastOtime):
                lastBtime = lastOtime+1
            lastBplace = int(button[2:])

    output.write("Case #"+str(i)+": "+str(max(lastBtime, lastOtime))+'\n')
            
