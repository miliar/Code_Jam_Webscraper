#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# PonyExpress

# https://code.google.com/codejam/contest/8294486/dashboard#s=p2


from sys import stdin
from pprint import PrettyPrinter
from math import floor, ceil

from tryalgo.floyd_warshall import floyd_warshall

pp = PrettyPrinter()

def readint():
    return int(stdin.readline())

def readints():
    return list(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()


def div_round_up(x, y):
    if x % y == 0:
        return x // y
    else:
        return (x // y) + 1


def solve(n, e, s, d):
    # first compute distances in graph
    for row in d:
        for i in range(n):
            if row[i] == -1:
                row[i] = float('inf')
    floyd_warshall(d)
    N = range(n)
    a = [[0 for j in N] for i in N]
    for i in range(n):
        for j in range(n):
            if d[i][j] <= e[i]:
                a[i][j] = d[i][j] / s[i]
            else:
                a[i][j] = float('inf')
    floyd_warshall(a)
    return a

for test in range(readint()):
    n, q = readints()
    e = [0] * n
    s = [0] * n
    for i in range(n):
        e[i], s[i] = readints()
    d = [readints() for _ in range(n)]
    a = solve(n, e, s, d)
    print("Case #%i:" % (test+1), end='')
    for _ in range(q):
        u, v = readints()
        time =  a[u-1][v-1]
        if time == float('inf'):
            time = -1
        print(" %f" % time, end='')
    print()


