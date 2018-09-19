#!/usr/bin/env python
#coding=utf-8

import sys
import math
input = file("C-small-attempt0.in","r")
#input = file("input.txt","r")

case = int(input.readline())
for ca in range(case):
    res = 0
    deck = int(input.readline())
    line = input.readline().split(" ")
    n = int(line[0])
    dl = []
    dc = []
    for i in range(n):
        dl.append(int(line[i+1]))

    shu = [0]*deck
    dc = range(deck)

    remain = deck
    index = 1
    for i in range(deck):
        index+=(i)
        index%=remain
   
        shu[i] = dc[index]
        remain -=1
        dc.remove(shu[i])

    ans=[0]*deck

    for i in range(deck):
        ans[shu[i]]=i+1
    bans = ans[1:]
    bans.append(ans[0])
    print "Case #"+str(ca+1)+": ",
    for i in range(n):
        print bans[dl[i]-1],
    print

    
    
    
            
    


