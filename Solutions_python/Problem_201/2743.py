#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('C-small-1-attempt0.in','r') as f: lines = f.read().splitlines()
cn = 1
for r in lines[1:]:
    N,K = r.split()
    S = [0 for _ in range(int(N))]
    L = [i for i in range(int(N))]
    R = [i for i in range(int(N)-1,-1,-1)]
    for i in range(int(K)):
        maxfit, maxfitpos = -1, -1
        for j in range(int(N)):
            if S[j]!=1:
                if maxfit < min(L[j],R[j]): 
                    maxfit=min(L[j],R[j])
                    maxfitpos = j
                elif maxfit == min(L[j],R[j]):
                    if max(L[j],R[j]) > max(L[maxfitpos],R[maxfitpos]): maxfitpos = j                  
        if i==(int(K)-1): 
            print 'Case #{}: {} {}'.format(cn, max(L[maxfitpos],R[maxfitpos]), min(L[maxfitpos],R[maxfitpos])) 
            break
        S[maxfitpos] = 1
        k = maxfitpos+1
        while (k<=(int(N)-1) and S[k]!=1):
            L[k] -= L[maxfitpos]+1
            k += 1            
        w = maxfitpos-1
        while (w>=0 and S[w]!=1):
            R[w] -= R[maxfitpos]+1
            w -= 1    
    cn += 1            