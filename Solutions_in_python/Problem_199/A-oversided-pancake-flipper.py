#!/usr/bin/env python

from __future__ import division, print_function
import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        S, K = sys.stdin.readline().split()
        S = list(S)
        K = int(K)

        count = 0

        for j in range(0, len(S) - K + 1):
            if S[j] == '-':
                count += 1
                for k in range(K):
                    S[j + k] = '+' if S[j + k] == '-' else '-'

        if len(set(S)) == 1:
            print('Case #%d: %d' % (i + 1, count))
        else:
            print('Case #%d: IMPOSSIBLE' % (i + 1))