#!/usr/bin/python
import sys
from math import pow
f = open('bull.txt', 'r')
first = int(f.readline())
count = 0
for line in f:
    ints = [int(i) for i in line.split()]
    r,t = ints[0],ints[1]
    result = 0
    while ( t > 0 ):
        lite = pow (r+1,2) - pow(r,2)
        t = t-lite
        if (t < 0):
            break
        r += 2
        result += 1
    count += 1
    print "Case #%d: %d" % (count,result)
