#!/usr/bin/python2.6

import os, sys, math

file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    N = int(file.readline())
    count = 0
    if N != 0:
        pairs = list()
        for i in range(N):
            A, B = tuple([int(k) for k in file.readline().split()])
            pairs.append((A, B))
        pairs.sort()
        left = list()
        right = list()
        for A, B in pairs:
            left.append(A)
            pos = len(right)
            for i in range(len(right)):
                if right[i] > B:
                    pos = i
                    break
            count = count + len(right)-pos
            right.insert(pos, B)
    print "Case #"+str(test+1)+": "+str(count)

file.close()
