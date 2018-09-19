#! /usr/bin/python

import sys

if __name__ == "__main__":
	cases = int(sys.stdin.readline())
	for case in xrange(1,cases+1):
		N = int(sys.stdin.readline())
		wires = []
		for i in xrange(N):
			wires.append(map(int,sys.stdin.readline().strip().split()))
		overlap = 0
		for i in xrange(N):
			for j in xrange(i+1,N):
				ia,ib = wires[i]
				ja,jb = wires[j]
				if ia <= ja and ib >= jb:
					overlap += 1
				elif ia >= ja and ib <= jb:
					overlap += 1
		print "Case #%d: %d" % (case, overlap)
