#!/usr/bin/python3

import sys
import math
from functools import reduce

def flip(l, p, k):
    for p in range(p, p+k):
        if l[p] == '+':
            l[p] = '-'
        else:
            l[p] = '+'


def solve(l, k):
    ll = len(l)
    l = list(l)
    flips = 0
    pos = 0

    while True:
        while l[pos] == '+':
            pos += 1
            if pos >= ll:
                pos = -1
                break

        p = pos
        if p == -1:
            return flips
        if p + k > ll:
            return None

        flip(l, p, k)
        flips += 1

    return 0

def main():
    nb = int(get_line())
    for case_id in range(1, nb + 1):
        l = get_line()
        ll = l.split(' ')[0]
        k = int(l.split(' ')[1])

        ret = solve(ll, k)

        if ret == None:
            l = 'IMPOSSIBLE'
        else:
            l = str(ret)

        print('Case #%d: %s' %(case_id, l), file = o)

def get_line():
    return f.readline().strip()

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    (f, o) = open_files()
    main()

