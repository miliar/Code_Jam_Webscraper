#!/usr/bin/env python2.6

import sys

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_line():
    return sys.stdin.readline().strip()

def solve():
    X = read_ints()
    N, S, p, t = X[0], X[1], X[2], X[3:]
    max = 0
    for total in t:
        x = total / 3
        if total % 3 == 0:
            r = (x, x, x)
            if x >= p:
                max +=1
            elif S > 0 and x > 0 and x + 1 >= p:
                max +=1
                S -= 1
        elif total % 3 == 1:
            r = (x + 1, x, x)
            if x + 1 >= p:
                max += 1                
        else:
            r = (x + 1, x + 1, x)
            if x + 1 >= p:
                max += 1
            elif S > 0 and x + 2 >= p:
                max += 1
                S -= 1
    print max


def main():
    T = read_int()
    
    for case in xrange(1, T + 1):
        print 'Case #%d:' % case,
        solve()

if __name__ == '__main__':
    main()
