#!/usr/bin/env python
# encoding: utf-8
"""
snapper-chain.py - Google Code Jam 2010

Copyright (c) 2010 David Jacot. All rights reserved.
"""

import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
	    print "usage: snapper-chain.py <filename>"
	    sys.exit()
	    
	with open(sys.argv[1]) as f:
	    # Read the number of problems
	    t = int(f.readline())
	    
	    # For each problem
	    for i, line in enumerate(f):
	        n, k = line.split()
	        n, k = int(n), int(k)
	        
	        n2 = 2**n
	        k %= n2
	        
	        if k == n2-1:
	            print "Case #%d: ON" % (i+1)
	        else:
	            print "Case #%d: OFF" % (i+1)

