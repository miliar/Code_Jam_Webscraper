# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 17:44:55 2017

@author: xiaominzhang
"""

import numpy as np
out = []
path = './A-small-attempt1.in'

def flip(s,start,k):
    for i in range(k):
        if s[start+i] == '+':
            s[start+i] = '-'
        else:
            s[start+i] = '+'
    return s

def calFlipNumber(s,k,n):
    if '-' not in s:
        return n
    else:
        start = s.index('-')
        if len(s) - start  < k:
            return 'IMPOSSIBLE'
        else:
            s = flip(s,start,k)
            n+=1
            return calFlipNumber(s,k,n)
        
        

with open(path, "r") as in_file:
    line = in_file.next()
    T = int(line.strip())
    for i in range(T):
        s, k = in_file.next().split()
        s = list(s)
        k = int(k)
        n = 0
        flipnumber = calFlipNumber(s,k,n)
        out.append(flipnumber)

outpath = './out.txt'
out_file = open(outpath, "w")
for i in range(T):
    out_file.write('Case #' + str(i+1)+ ': ' + str(out[i]) +'\n') 
out_file.close()