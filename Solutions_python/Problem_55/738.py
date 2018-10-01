#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Johan Musaeus Bruun, 20100508

# ./C.py < C-small-attempt0.in | tee C-small.out

import sys

def main(fin):
	T = int(fin.readline())
	# T = number of test cases
	
	for t in range(1,T+1):
		R, k, N = map(int, fin.readline().split())
		q = map(int, fin.readline().split())
		#print q
		#print "R=%d, k=%d, N=%d" % (R,k,N)
		sum = 0
		pos = 0
		for r in range(R):
			earnings, pos = nextRide(q,pos,k,N)
			sum += earnings
			#print "%d %d" % (r, earnings)
		print "Case #%d: %s" % (t, sum)
	exit()


def nextRide(q,pos,k,N):
	startpos = pos
	booked = q[pos]
	pos = (pos + 1) % N
	run = True
	if pos == startpos:
		run = False
	while run:
		nextgroup = q[pos]
		if booked + nextgroup <= k:
			booked += nextgroup
			pos = (pos + 1) % N
			if pos == startpos:
				run = False
		else:
			run = False
	earnings = booked
	return earnings, pos

################################################################

if __name__ == '__main__':
	try:
		#fin = open("A-test.in", 'r')
		fin = sys.stdin 
		main(fin)
	except IOError:
		print "File I/O error!"
