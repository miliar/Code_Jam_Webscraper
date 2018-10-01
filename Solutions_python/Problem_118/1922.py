#!/usr/bin/env python

import math

def is_palindrom(n):
    return str(n) == str(n)[::-1]

def test_case(lower, upper):
    l = int(math.ceil(math.sqrt(lower)))
    u = int(math.floor(math.sqrt(upper)))
    res = 0
    for i in xrange(l,u + 1):
        if is_palindrom(i) and is_palindrom(i*i):
            res += 1
    return res

with open('input.in') as f:
    n = int(f.readline())
    i = 0
    for case in xrange(n):
        bounds = f.readline().split(' ')
        res = test_case(int(bounds[0]), int(bounds[1]))
        print 'Case #%d: %d' % (case + 1, res)
