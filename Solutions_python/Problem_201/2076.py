# coding: utf-8

import os, sys, re, string
import math,random

def calc(s):
    v = s >> 1
    if (s & 1) == 1:
        return (v, v, v, v)
    if s == 0:
        return (0, 0, 0, 0)
    if s == 2:
        return (0, 1, 0, 1)
    return (v - 1, v, v - 1, v)


def solve(n, k):
    last = calc(n)
    openlist = [last]
    #print 'S', openlist, n, k
    for i in xrange(k):
        last = openlist[0]
        openlist = openlist[1:] + [calc(last[0]), calc(last[1])]
        openlist.sort(lambda a,b: b[3] - a[3] if a[2] == b[2] else b[2] - a[2])
        #print last, openlist
    return last


def main():
    t = int(sys.stdin.readline())
    for i in xrange(1, t + 1):
        n, k = map(int, sys.stdin.readline().split(' '))
        result = solve(n, k)
        print 'Case #{0}: {1} {2}'.format(i, result[3], result[2])

if __name__ == '__main__':
    main()


