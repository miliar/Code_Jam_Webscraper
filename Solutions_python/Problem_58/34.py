#!/usr/bin/env python
# encoding: utf-8

import sys

def _solve(A, B):
    # if A == 1:
    #     return B % 2
    # elif B == 1:
    #     return A % 2  
    if A == B:
        return False
    elif A > B:
        if A % B:
            km = A/B
        else:
            km = A/B-1
        for k in xrange(km, 0, -1):
            if not _solve(A-k*B, B):
                return True
    else:
        if B % A:
            km = B/A
        else:
            km = B/A-1
        for k in xrange(km, 0, -1):
            if not _solve(A, B-k*A):
                return True
    
    return False
        
def solve(A1, A2, B1, B2):
    A = A2 - A1
    B = B2 - B1

    nb = 0
    for i in xrange(A1, A1+A+1):
        for j in xrange(B1, B1+B+1):
            if _solve(i, j):
                nb += 1
    return nb

#print _solve(5, 8)
#print _solve(12, 51)

T = int(sys.stdin.readline())
for i in xrange(1, T+1):
    args = map(int, sys.stdin.readline().split())
    print "Case #%d: %d" % (i, solve(*args))