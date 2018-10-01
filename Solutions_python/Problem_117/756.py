#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

T =  int(sys.stdin.readline())

def cross(n, m, lawn, size):
    row = lawn[n]
    col = [lawn[y][m] for y in range(size[0])]
    target = lawn[n][m]
    if (target == max(row)):
        return True
    elif (target == max(col)):
        return True
    else:
        return False


def judge(lawn, size):
    for n in range(0, size[0]):
        for m in range(0, size[1]):
            if (cross(n, m, lawn, size) == False):
                return False
    return True


for x in range(0, T):
    size = map(int, sys.stdin.readline().split())
    lawn = [map(int, (sys.stdin.readline().split())) for xxx in range(size[0])]

    if (judge(lawn, size) == True):
        print "Case #%d: YES" % (x+1)
    else:
        print "Case #%d: NO" % (x+1)
