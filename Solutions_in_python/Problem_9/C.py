#!/usr/bin/env python

import os
import sys
import bisect

def main():
    for ii in xrange(int(raw_input())):
	
		K = int(raw_input())
		
		d = map(int, raw_input().split(" "))[1:]
		
		p = range(K)
		
		r = range(K)
		
		t = 0
		for i in range(K):
			t += i
			t %= len(p)
#			print p[t]
			r[p[t]] = i+1
			p.remove(p[t])
		
		
		print "Case #%d:" % (ii+1), 
		for i in d:
			print r[i-1],
		print ""
		#print "Case #%d: %d" % (ii+1, c)
			

if __name__ == '__main__':
    main()	
	
	