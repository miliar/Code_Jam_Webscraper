#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def count(s):
    a, b, k = map(int, s.split(' '))
    if k >= a and k >=b:
        return str(a*b)
    res = 0
    for i in xrange(0, a):
        for j in xrange(0, b):
            if i&j < k:
                res += 1
    return str(res)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        buf = f.read()
    t = buf.split("\n")
    nb_boards = int(t[0])
    t = t[1:]
    for k in xrange(0, nb_boards):
        print "Case #%d: %s"%(k+1, count(t[k]))
