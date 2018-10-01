#!/usr/bin/python

import os
import sys
import math


infile = open(sys.argv[1])
T = int(infile.readline())

for i in range(T):
    N = int(infile.readline())
    left = []
    right = []
    for j in range(N):
        line = infile.readline()
        items = line.split(' ')
        left.append(int(items[0]))
        right.append(int(items[1]))
    count = 0
    for k in range(N):
        for j in range(k, N):
            if (left[k] - left[j]) * (right[k] - right[j]) < 0:
                count += 1
    print 'Case #' + str(i+1) + ':', count




