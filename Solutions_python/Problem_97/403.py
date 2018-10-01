#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline())
for i in range(1, T+1):
    l = sys.stdin.readline()
    cols = l.split(None)
    A = int(cols[0])
    B = int(cols[1])
    flags = [0] * (B+1)
    counter = 0

    if B < 10:
        digits = 1
    elif B < 100:
        digits = 2
    elif B < 1000:
        digits = 3
    elif B < 10000:
        digits = 4
    elif B < 100000:
        digits = 5
    elif B < 1000000:
        digits = 6
    else:
        digits = 7
    coeff = 10 ** (digits - 1)

    for k in range(A, B+1):
        if flags[k] == 0:
            flags[k] = 1
            tmp_cnt = 1
            # check recycle numbers
            tmp = k
            for p in range(digits - 1):
                tmp = tmp / 10 + (tmp % 10) * coeff
                if A <= tmp <= B:
                    if flags[tmp] == 1:
                        # loop
                        break
                    else:
                        flags[tmp] = 1
                        tmp_cnt += 1
            # How many pairs?
            counter += tmp_cnt * (tmp_cnt - 1) / 2

    print "Case #%d:" % i, counter
