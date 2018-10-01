#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-08 14:44:21

import sys

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
    (n,k) = [ int(x) for x in f.readline().split()]
    #print n,k

    # 0 Power 1 ON/OFF
    snapper = [ [False, False] for x in range(n+1) ]
    snapper[0] = [True, True]
    snapper[1] = [True, False]
    #print snapper

    i = 0
    while i < k:
        for x in range(1,n+1):
            if snapper[x][0]:
                snapper[x][1] = not snapper[x][1]
            if snapper[x-1][0] and snapper[x-1][1]:
                snapper[x][0] = True
            else:
                snapper[x][0] = False
        i += 1

    if snapper[n][0] and snapper[n][1]:
        print "Case #%d: %s"%(nncase+1,"ON")
    else:
        print "Case #%d: %s"%(nncase+1,"OFF")
    
f.close()
