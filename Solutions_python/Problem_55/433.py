#!/usr/bin/python2.6

import os, sys, math

file = open(sys.argv[1] , 'r')
nbr_testcases = int(file.readline())

for test in range(nbr_testcases):
    R, k, N = tuple([int(i) for i in file.readline().split()])
    groups = [int(i) for i in file.readline().split()]
    newgroups = []
    money = 0
    for i in range(R):
        count = 0
        while (count < k and len(groups)>0):
            g = groups[0]
            if g + count > k:
                break
            else:
                count += g
                newgroups.append(groups.pop(0))
                money += g
        groups.extend(newgroups)
        newgroups = []
    print "Case #"+str(test+1)+": "+str(money)

file.close()
