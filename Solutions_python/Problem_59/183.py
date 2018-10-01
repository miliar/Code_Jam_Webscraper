# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/artiom/.spyder/.temp.py
"""

    
import sys
f = open(sys.argv[1], "rt")
T =  int(f.next().strip())
for t in range(T):
    folders = dict()
    l = f.next().strip()

    M, N = map(int, l.split())
    for m in range(M):
        v = folders
        for d in f.next().strip().split('/')[1:]:
            if not v.has_key(d):
                v[d] = dict()
            v = v[d]
    count = 0
    for n in range(N):
        v = folders
        for d in f.next().strip().split('/')[1:]:
            if not v.has_key(d):
                v[d] = dict()
                count = count+1
            v = v[d]

    print 'Case #%d: %d' %(t+1, count)
        
