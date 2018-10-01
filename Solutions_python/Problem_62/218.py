#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-23 18:23:07

import sys

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
    n = int(f.readline())
    #print n,k

    p = [] 
    for i in range(n):
        p.append([int(x) for x in f.readline().split()])

    count = 0

    #if n == 2:
    #    if p[0][0] > p[1][0] and p[0][1] > p[1][1]:
    #        count = 0
    #    elif p[0][0] < p[1][0] and p[0][1] < p[1][1]: 
    #        count = 0
    #    else:
    #        count = 1
    #elif n > 2:
    for i in range(n):
        for j in range(i+1,n):
            if p[i][0] > p[j][0] and p[i][1] < p[j][1]:
                count += 1
            elif p[i][0] < p[j][0] and p[i][1] > p[j][1]: 
                count += 1

    print "Case #%d: %d"%(nncase+1, count)
    
f.close()
