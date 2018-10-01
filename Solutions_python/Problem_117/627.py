import os
import sys


entries = int(sys.stdin.readline())

for case in range(1, entries + 1):
	rows, cols = sys.stdin.readline().strip().split()
	rows = int(rows)
	cols = int(cols)
	lawn = [sys.stdin.readline().strip().split() for x in range(rows)]
	lawn2 = zip(*lawn)
	
	def check():
		for y in xrange(rows):
			for x in xrange(cols):
				h = lawn[y][x]
				if max(lawn[y]) > h and max(lawn2[x]) > h:
					return False
		return True
	if check():
		print "Case #%d: YES" % case
	else:
		print "Case #%d: NO" % case

