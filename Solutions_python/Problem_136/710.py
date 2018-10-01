#!/usr/bin/env python
#coding=utf-8
##inPath = 'test.in'
##outPath = 'test.out'B-small-attempt0.in
inPath = 'B-large.in'
outPath = "B-large.out"

def cookie(c, f, x):
    smallest = x / 2
    farmTotal = 0
    farmNum = 0
    t1 = x / 2
    while farmTotal <= smallest:
        t2 = c / (farmNum * f + 2) + x / (2 + (farmNum + 1) * f)
        if t2 < t1:
            smallest = smallest - t1 + t2
        farmTotal += c / (farmNum * f + 2)
        farmNum += 1
        t1 = x / (2 + farmNum * f)
    return smallest

with open(outPath,'w') as outf:
    with open(inPath) as inf:
        n = int(inf.readline().strip()) 
        for case in xrange(1, n+1):
            print case
            c, f, x = [float(i) for i in inf.readline().strip().split()]            
            outf.write("Case #" + str(case) + ": %.7f" %cookie(c, f, x) + '\n')
    inf.close()
outf.close()
