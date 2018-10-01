#!/usr/bin/python
import sys

t = int(sys.stdin.readline())
for x in range(1, t + 1):
    n = int(sys.stdin.readline())
    N = [float(i) for i in sys.stdin.readline().split()]
    K = [float(i) for i in sys.stdin.readline().split()]
    NS = sorted(N)
    KS = sorted(K) 
    y = 0
    z = 0
    for i in range(len(NS) - 1, -1, -1):
        if NS[i] > KS[i]:
            z = z + 1
            del KS[0]
        else:
            del KS[-1]
        del NS[i]
    NS = sorted(N)
    KS = sorted(K)
    while(len(NS) > 0):
        if NS[0] < KS[0]:
            del KS[-1]
        else:
            y = y + 1
            del KS[0]
        del NS[0]
    print('Case #%d: %d %d' %(x, y, z))
            
