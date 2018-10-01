#!/usr/bin/env python3
import sys

def get_line():
	return sys.stdin.readline().strip()

def equal_lawns(lawn, pattern):
	for i in range(len(lawn)):
		for j in range(len(lawn[0])):
			if lawn[i][j] != pattern[i][j]:
				return False
	return True

def can_mown_the_lawn(pattern):
	n, m = len(pattern), len(pattern[0])
	lawn = [[100 for _ in range(m)] for _ in range(n)]
	# Try horizontals
	for i in range(n):
		h = max(pattern[i])
		#print('Max horiz', i, 'is', h)
		for j in range(m):
			lawn[i][j] = min(h, lawn[i][j])
	# Try verticals
	for j in range(m):
		h = 0
		for i in range(n):
			h = max(h, pattern[i][j])
		#print('Max vert', j, 'is', h)
		for i in range(n):
			lawn[i][j] = min(h, lawn[i][j])
	#print('Pattern', pattern)
	#print('Lawn', lawn)
	equal = equal_lawns(lawn, pattern)
	return 'YES' if equal else 'NO'

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for case in range(ncases):
		n, m = [int(x) for x in get_line().split(' ')]
		lawn = []
		for _ in range(n):
			lawn.append([int(x) for x in get_line().split(' ')])
		result = can_mown_the_lawn(lawn)
		print('Case #', case + 1, ': ', result, sep='')
