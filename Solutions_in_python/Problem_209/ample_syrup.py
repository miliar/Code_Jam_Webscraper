#!/bin/python3

import sys
import math

def getKey(item):
    return item[0]
    
def max_syrup(pans, k, base = False):
    n = len(pans)
    maxa = 0
    if k == 0:
        return 0
    if n == k:
        if base:
            maxa += pans[0][0]**2
        for pan in pans:
            maxa += 2*pan[0]*pan[1]
        return maxa
    for i in range(n-k+1):
        temp = 0
        if base:
            temp += pans[i][0]**2
        temp += 2*pans[i][0]*pans[i][1]
        temp += max_syrup(pans[i+1:], k-1)
        if temp > maxa:
            maxa = temp
    return maxa
    
t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split()
    n = int(n)
    k = int(k)
    pancakes = []
    for i in range(n):
        r, h = input().strip().split()
        r = int(r)
        h = int(h)
        pancakes.append((r, h))
    pancakes.sort(key = getKey, reverse = True)
    result = max_syrup(pancakes, k, True)
    print("Case #" + str(a0+1) + ": " + str(math.pi*result))