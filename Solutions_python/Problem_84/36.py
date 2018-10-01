#!/usr/bin/env python
import sys
from numpy import *

def read_n(a):
    n = int(a[0])
    return a[1:n+1], a[n+1:]

def solve():
    R, C = map(int, sys.stdin.readline().split())
    d = [list(sys.stdin.readline().strip()) for i in range(R)]
    # n = sum(i.count('#') for i in d)
    while (True):
        for i in range(R):
            try:
                pos = d[i].index('#')
                break
            except ValueError:
                pos = -1
        if pos==-1:
            return '\n'.join(''.join(i) for i in d)
        if not (i+1<R and pos+1<C):
            return False
        if d[i][pos] == d[i][pos+1] == d[i+1][pos] == d[i+1][pos+1] == '#':
            d[i][pos] = '/'
            d[i][pos+1] = '\\'
            d[i+1][pos] = '\\'
            d[i+1][pos+1] = '/'
        else:
            return False


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        print "Case #{}:".format(t+1)
        print solve() or 'Impossible'

