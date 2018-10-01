# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:02:52 2017

@author: Jo
"""
import numpy as np

def a(m):
    s = ''
    if int(m[0]) == 0:
        l = 1
    else:
        l = 0
    for i in np.arange(l,len(m)):
        s+= m[i]
    return s

T = int(input())
N = []

for i in np.arange(T):
    N.append(list(input()))
    
M = list(np.copy(N))
    
for j in np.arange(T):
    if len(N[j]) == 1:
        print('Case #' + str( j+1) + ':' + ' ' + str(a(M[j])))
    
    else:
        for l in np.arange(1,len(N[j])):
            if N[j][-1-l] > N[j][-l]:
                M[j][-1-l] = str(int(M[j][-1-l]) - 1)
                for o in np.arange(l):
                    M[j][-o-1] = '9'
        print('Case #' + str(j + 1) + ':' + ' ' + str(a(M[j])))