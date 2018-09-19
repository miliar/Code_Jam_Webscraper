#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for i in range(T):
        N = int(sys.stdin.readline())
        naomi = sorted(map(float, sys.stdin.readline().split()))
        ken = sorted(map(float, sys.stdin.readline().split()))
        
        
        # Calculate War
        war = 0
        x = ken[:]
        
        for n in reversed(naomi):
            for j, k in enumerate(x):
                if k > n:
                    x.pop(j)
                    break
            else:
                war += 1
        
        
        # Calculate Deceitful War
        deceitful_war = 0
        x = ken[:]
        
        for n in reversed(naomi):
            for j, k in reversed(list(enumerate(x))):
                if n > k:
                    x.pop(j)
                    deceitful_war += 1
                    break
        
        
        print('Case #%d: %d %d' % (i + 1, deceitful_war, war))
