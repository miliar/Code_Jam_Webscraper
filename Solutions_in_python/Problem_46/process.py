#!python

'''
google code jam 2009
round 2
problem a

'''

timeit = 1
debugv = 1

from sys import stdin, stderr
import time


def doCase(case):
	N = int(stdin.readline())
	# we index from 0, no problem
	rows = [stdin.readline() for i in xrange(N)]
	minrows = [max(0,row.rfind("1")) for row in rows]
	
	moves = 0
	for i in xrange(N):
		for j in xrange(i,N):
			if minrows[j] <= i:
				moves += j-i
				val = minrows[j]
				minrows[j:j+1] = []
				minrows[i:i] = [val]
				break
	
	print "Case #%d: %d" % (case, moves)

def main():
	testCases = int(stdin.readline())
	for case in xrange(1,testCases+1):
		doCase(case)

def debug(m):
	if debugv:
		print >>stderr, m

start = time.clock()

main()

if timeit: print >>stderr, "time: %s" % (time.clock() - start)

