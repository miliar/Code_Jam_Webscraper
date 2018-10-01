#!/usr/bin/python
import sys, operator, time

lines = sys.stdin.read().split('\n')[1:]

case = 0

def gem_replace(gems):
	height = len(gems)
	for i in range(len(gems)):
		width = len(gems[i])
		for j in range(len(gems[i])):
			if gems[i][j] == '#':
				if i + 1 < height and j + 1 < width and gems[i][j+1] == '#' and gems[i+1][j] == '#' and gems[i+1][j+1] == '#':
					gems[i][j] = '/'
					gems[i][j+1] = '\\'
					gems[i+1][j] = '\\'
					gems[i+1][j+1] = '/'
				else:
					return False
	return True

while lines:
	case += 1
	line = lines.pop(0)
	if not line:
		continue

	r, c = [int(x) for x in line.split()]
	gems = [list(l) for l in lines[:r]]
	result = gem_replace(gems)

	print "Case #%d:" % case
	if result:
		for line in gems:
			print ''.join(line)
			
	else:
		print "Impossible"

	del lines[:r]
