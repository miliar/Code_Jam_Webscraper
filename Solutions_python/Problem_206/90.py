#!/usr/bin/env pypy3
# -*- coding: utf-8 -*-
# google code jam - c.durr - 2017

# Steed2CruiseControl
# https://code.google.com/codejam/contest/8294486/dashboard


from sys import stdin
from pprint import PrettyPrinter
from math import floor, ceil

pp = PrettyPrinter()

def readint():
    return int(stdin.readline())

def readints():
    return tuple(map(int, stdin.readline().split()))

def readstring():
    return stdin.readline().strip()

def readstrings():
    return stdin.readline().split()


def div_round_up(x, y):
    if x % y == 0:
        return x // y
    else:
        return (x // y) + 1


def solve(D, H):
    """complexity: O(n)
    compute maximum arrival time among all horses
    """
    latest = 0
    for k, s in H:
        time = (D-k)/s
        if time > latest:
            latest = time
    return D / latest


for test in range(readint()):
    d,n = readints()
    H = [readints() for i in range(n)]
    print("Case #%i: %f" % (test+1,  solve(d, H)))


