#!/usr/bin/env python
#coding=utf-8
import sys

input = file("A-large.in", "r")
#input = file("input.txt", "r")
case = int(input.readline())
#print case
d = {}
for c in range(case):
    n = int(input.readline())
#    print n
    s = 0
    base = 0
    for i in range(n):
        d[input.readline()] = base
    q = int(input.readline())
#    print q
    for i in range(q):
        t = input.readline()
        d[t] = base+1
        if base not in d.values():
            s+=1
            base += 1
            d[t] = base+1
    print "Case #"+str(c+1)+": "+str(s)
    d.clear()
