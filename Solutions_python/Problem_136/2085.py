#!/usr/bin/env python 

import sys

T = input()

for t in range(1, T+1): 
    a = 2.0
    C, F, X = map(float, raw_input().split())
    base = X / a
    S = 0
    i = 0
    M = base
    while True: 
        S += C / (a + i*F)
        value = S + X/ (a + (i+1) * F)
        if value < M: 
            M = value
        else: 
            break
        i += 1
    print 'Case #%d: %.7f' %(t, M)
