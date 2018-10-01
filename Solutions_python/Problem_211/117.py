#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 09:53:08 2017

@author: marshi
"""

import numpy as np

def core_training_small(n,k,u,p):
    p = sorted(p)
    p.append(1.)
    
    for i in range(1,len(p)):
        if ((p[i]-p[i-1])*i) <= u:
            u -= (p[i]-p[i-1])*i
            for j in range(i):
                p[j] = p[i]
        else:
            for j in range(i):
                p[j] += u/i
            break
    return np.product(p)
    
if 0:
    n,k = 2,2
    u = 1.
    p = [0.,0.]
   
    print(core_training_small(n,k,u,p))
    
        
    
else:
    t = int(input())
    for i in range(t):
        n,k = map(int, input().split(' '))
        u = float(input())
        p = map(float, input().split(' '))
    
        print("Case #%d: %.9f"%(i+1, core_training_small(n,k,u,p)))