#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def read_attempt():
    row = int(sys.stdin.readline())
    arr = []
    for i in xrange(4):
        arr.append([int(x) for x in sys.stdin.readline().strip().split()])
    return row, arr

def solve(row1, arr1, row2, arr2):
    row1 -= 1
    row2 -= 1
    return set(arr1[row1]) & set(arr2[row2])

    


test_count = int(sys.stdin.readline())
for i in xrange(test_count):
    row1, arr1 = read_attempt()
    row2, arr2 = read_attempt()
    var = solve(row1, arr1, row2, arr2)
    if len(var) > 1:
        print "Case #{}: Bad magician!".format(i + 1)
    elif not var:
        print "Case #{}: Volunteer cheated!".format(i + 1)
    else:
        print "Case #{}: {}".format(i + 1, var.pop())
