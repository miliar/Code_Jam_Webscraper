#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())

def convert(lines, r, c):
	try:
		if lines[r][c] == '#' and lines[r][c+1] == '#' and lines[r+1][c] == '#' and lines[r+1][c+1] == '#':
			lines[r][c] = '/'
			lines[r][c+1] = '\\'
			lines[r+1][c] = '\\'
			lines[r+1][c+1] = '/'
			return True
	except Exception:
		return False
	return False

def hasSharp(lines):
	for line in lines:
		for c in line:
			if c == '#':
				return True
	return False

for t in range(T):
	R, C  = sys.stdin.readline().split()
	lines = []
	for r in range(int(R)):
		line = [x for x in sys.stdin.readline().rstrip()]
		lines.append(line)

	ret = True
	for r in range(int(R)):
		for c in range(int(C)):
			if lines[r][c] == '#':
				if not convert(lines, r, c):
					ret = False
			if not ret: break
		if not ret: break

	print 'Case #%s:' % (t+1)
	if ret == False or hasSharp(lines):
		print 'Impossible'
	else:
		for line in lines:
			print ''.join(line)
