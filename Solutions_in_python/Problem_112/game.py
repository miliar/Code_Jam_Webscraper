#! /usr/bin/env python

from sys import stdin
import numpy as np

ntest = input()

for test in range(ntest):
    n = input()
    l = np.array([int(i) for i in stdin.readline().strip().split()])
    p = np.array([int(i) for i in stdin.readline().strip().split()])
        
    print "Case #%d: %s" % (test+1, ' '.join(['%d' % i for i in np.argsort(-p, kind='mergesort')]))