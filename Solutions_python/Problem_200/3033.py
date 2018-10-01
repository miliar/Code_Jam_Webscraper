#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


def tidy(n):
    if n < 10:
        return n

    nlist = list(str(n))
    index, tidy_digit = 0, True
    for i in range(1, len(nlist)):
        # print(str(nlist[i-1] > nlist[i]), tidy_digit, nlist[i-1], nlist[i])
        if tidy_digit & (int(nlist[i-1]) > int(nlist[i])):
            tidy_digit = False
            index = nlist.index(nlist[i-1]) + 1
            break
    for i in range(index, len(nlist)):
            nlist[i] = "0"
    if tidy_digit:
        return n
    return int(''.join(nlist)) - 1


with sys.stdin as f:
    T = int(f.readline())
    for i in range(T):
        n = int(f.readline())
        print("Case #" + str(i+1) + ": " + str(tidy(n)))
