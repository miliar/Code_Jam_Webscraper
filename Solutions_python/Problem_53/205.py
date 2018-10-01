#!/usr/bin/python

import sys

T = int(raw_input())
for case in range(T):
    N, K = map(int, raw_input().split())
    temp = 2 ** N
    if K % temp == temp - 1:
        print 'Case #%d: ON' % (case + 1)
    else:
        print 'Case #%d: OFF' % (case + 1)
