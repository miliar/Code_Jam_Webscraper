#!/usr/bin/env python
# encoding: utf-8
"""
CandySplitting.py

Created by Graham Dennis on 2011-05-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys, operator


def main():
    f = open(sys.argv[1])
    T = int(f.readline())
    
    for t in xrange(T):
        N = int(f.readline())
        candies = map(int, f.readline().split())
        result = None
        if reduce(operator.xor, candies) != 0:
            result = "NO"
        else:
            candies.sort()
            result = str(sum(candies[1:]))
        print "Case #%i: %s" % (t+1, result)

if __name__ == "__main__":
    sys.exit(main())
