#!/usr/bin/python

from sys import stdin

"""
cases:
    3n+0: n   + n   + n
          n-1 + n   + n+1 (*)
    3n+1: n   + n   + n+1
          n-1 + n+1 + n+1 (*)
    3n+2: n   + n   + n+2 (*)
          n   + n+1 + n+1
"""

T = int(stdin.readline())
for i in range(T):
    line = map(int, stdin.readline().split())
    [N, S, p], t = line[:3], line[3:]
    #print 'N %d S %d p %d t %r'%(N,S,p,t)
    y = 0
    for s in t:
        n, r = s / 3, s % 3
        m = n + [0, 1, 1][r]
        #print 's %d n %d r %d m %d' % (s,n,r,m)
        if m >= p:
            y += 1
            #print 'not surprise y %d'%y
        elif m == p - 1 and r != 1 and S > 0 and n > 0:
            y += 1
            S -= 1
            #print 'surprise y %d S %d'%(y,S)
    print 'Case #%d: %d' % (i + 1, y)

