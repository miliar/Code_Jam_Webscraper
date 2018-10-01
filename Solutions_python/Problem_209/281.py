# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:56:02 2017

@author: Robbe Sneyders
"""

import numpy as np
import math

def answer(pancakes, k):
    
    pancakes = [[pancakes[i, 0], 2 * math.pi * pancakes[i, 0] * pancakes[i, 1]] for i in range(pancakes.shape[0])]
    
    pancakes = sorted(pancakes, key=lambda x: (x[1], x[0]))[::-1]
    pancakes = np.array(pancakes)
    
    maxr = np.max(pancakes[:k, 0])
    maxopp = math.pi * pow(maxr, 2)
    
    mopp = 0
    for i in range(k, pancakes.shape[0]):
        opp = math.pi * pow(pancakes[i, 0], 2)
        if opp - maxopp + pancakes[i, 1] > mopp:
            mopp = opp - maxopp + pancakes[i, 1]
        
    if mopp > pancakes[k-1, 1]:
        result = mopp + np.sum(pancakes[:(k-1), 1]) + maxopp
    else:
        result = maxopp + np.sum(pancakes[:k, 1])
    
    return result

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    
    pancakes = []
    for j in range(n):
        pancakes.append([int(s) for s in input().split(" ")])
    pancakes = np.array(pancakes)
        
    stack = answer(pancakes, k)
    print("Case #{}: {}".format(i, stack))