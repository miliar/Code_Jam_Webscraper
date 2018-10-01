# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:13:12 2017

@author: Henry
"""

def flipPankes(N, k):
    N = list(N)
    flips = 0
    for idx, i in enumerate(N):
        if i == '+':
            continue
        else:
            if idx + k > len(N):
                return 'IMPOSSIBLE'
            else:
                flips += 1
                for j in range(idx, idx+k):
                    if N[j] == '-':
                        N[j] = '+'
                    else:
                        N[j] = '-'
    return flips
                        
for i in range(int(input())):
    cakes, l = input().split()
    print('Case #{}: {}'.format(i+1, flipPankes(cakes, int(l))))