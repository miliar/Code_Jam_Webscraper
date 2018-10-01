#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys
from itertools import permutations

def toInt(d):
	return int("".join(str(i) for i in d))
	
def proc(d, n):

	t = []
	for i in permutations(d, len(d)):
		s = toInt(i)
		if s > n: t.append(s)
		
	if len(t):
		return sorted(t)[0]
	else:
		return proc(d+tuple([0]), n)

		
def main():
	fName = sys.argv[1]
	fIn = open("%s.in" % fName, 'r')
	fOut = open("%s.out" % fName, 'w')
	
	for i in xrange(int(fIn.next())):
		
		s = fIn.next().strip()
		d = tuple([int(j) for j in s])
				
		r = proc(d, toInt(d))
	
		fOut.write("Case #%s: %s\n" % (i+1, r))
		
if __name__ == '__main__': main()
