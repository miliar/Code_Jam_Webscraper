#!/usr/bin/python
# -*- coding: utf-8 -*-
    
# google code jam - c.durr - 2013
# Fair and Square
# brute force precomputing


def readInts(): return [int(i) for i in raw_input().split()]

def reverse(n):
    rev = 0
    while n>0:
        rev = 10*rev + (n%10)
        n /= 10
    return rev

MAX  = 10000001
nice = []
for i in range(MAX):
    ii = i*i
    if i==reverse(i) and ii==reverse(ii):
        nice.append(ii)
        
def binary_search(tab, x):
    # trouve plus petit i tel que tab[i]>=x
    lo = 0
    hi = len(tab)
    while lo < hi:
        mid = (lo+hi)//2
        if tab[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo

def solve(A, B):
    a = binary_search(nice, A)
    b = binary_search(nice,B+1)
    return b-a


for test in range(int(raw_input())):
    A,B = readInts()
    print 'Case #%d:' % (test+1), solve(A,B)
    
