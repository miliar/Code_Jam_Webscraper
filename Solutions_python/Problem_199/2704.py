# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def pancakesolver(s, K):
    t = []
    for i in range(len(s)):
        if s[i] == '+':
            t.append(1)
        else:
            t.append(0)
    
    turnover = 0
    L = len(s) - K
    for i in range(L+1):
        if t[i] == 1:
            continue
        else:
            turnover += 1
            for j in range(K):
                t[i+j] = 1 - t[i+j]
    if 0 in t:
        return -1        
    return turnover

T = int(raw_input())
for i in range(1, T+1):
    [s, k] = raw_input().split(' ')
    K = int(k)
    result = pancakesolver(s, K)
    if result == -1:
        print "Case #{}: {}".format(i, 'IMPOSSIBLE')
    else:
        print "Case #{}: {}".format(i, result)