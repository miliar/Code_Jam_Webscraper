#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for i in range(T):
        C, F, X = list(map(float, sys.stdin.readline().split()))
        
        n, t, r = 0, 0, 2
        
        while n + C < X:
            n += C
            t += C / r
            
            if (X - n + C) / (r + F) < (X - n) / r:
                n -= C
                r += F
            else:
                break
        
        t += (X - n) / r

        print('Case #%d: %.7f' % (i + 1, t))
