#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 23:30:41 2017

@author: lin
"""
from __future__ import print_function, division
import numpy as np

T = int(raw_input())  # read a line with a single integer
for case in xrange(1, T + 1):
    pancakes, flippersize = raw_input().split(" ")
    flippersize = int(flippersize)
    pancakes = np.array([int(pancake == '+')*2-1 for pancake in pancakes])
    N = len(pancakes)
    countflips = 0
    maxflips = N - flippersize + 1
    for i in xrange(maxflips):
        if pancakes[i] == -1:
            countflips += 1
            pancakes[i:i+flippersize] = pancakes[i:i+flippersize]*-1
    sum_pancakes = np.sum(pancakes)
    
    if sum_pancakes == N:
        flips = countflips
    else:
        flips = 'IMPOSSIBLE'
    print("Case #{0}: {1}".format(case, flips))