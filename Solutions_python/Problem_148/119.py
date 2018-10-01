#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys
import os

def main():
    T = int(sys.stdin.readline())
    for t in xrange(1, T+1):
        N, X = map(int, sys.stdin.readline().split())
        sizes = list(reversed(sorted(map(int, sys.stdin.readline().split()))))
        assert len(sizes) == N
        used = [False] * N
        ret = 0
        for i, v in enumerate(sizes):
            if used[i]:
                continue
            ret += 1
            used[i] = True
            for j in xrange(i+1, N):
                if not used[j] and sizes[j] + sizes[i] <= X:
                    used[j] = True
                    break
        print "Case #" + str(t) + ": " + str(ret)


if __name__ == '__main__':
    main()
