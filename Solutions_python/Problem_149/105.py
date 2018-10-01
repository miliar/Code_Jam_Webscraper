#!/usr/bin/python3

import sys
import math
EPS = sys.float_info.epsilon

def readi(): return int(sys.stdin.readline())
def readis(): return [int(x) for x in sys.stdin.readline().split()]

def case():
    N = readi()
    A = readis()
    mi = 0
    m = A[0]
    for i in range(N):
        if A[i] > m:
            m = A[i]
            mi = i
    M = N*N
    for t in range(1<<N):
        count = 0
        t |= (1 << mi)
        for i in range(N):
            for j in range(i+1,N):
                a = t & (1<<i)
                b = t & (1<<j)
                if a and b:
                    count += 1 if A[i] > A[j] else 0
                if a and not b:
                    count += 0
                if not a and b:
                    count += 1
                if not a and not b:
                    count += 1 if A[i] < A[j] else 0
        if count < M:
            M = count
    return M

T = readi()
for i in range(T):
    print("Case #%s: %s" % (1+i, case()))


    

