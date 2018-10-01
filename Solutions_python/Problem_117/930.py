#!/usr/bin/env python2.7

def solve(filename):
	inf = open(filename, "Ur")
	ouf = open("out", "w")
	l = inf.readlines()
	num = int(l.pop(0))
	for d in range(num):
		(n, m) = map(lambda x: int(x), l.pop(0).split())
		grid = []
		for x in range(n): grid.append(l.pop(0).split())
		run = True
		for x in range(n):
			for y in range(m):
				if not check(x, y, grid): 
					ouf.write("Case #" + str(d + 1) + ": NO\n")
					run = False
					break
			if not run: 
				break	
		if run: ouf.write("Case #" + str(d + 1) +  ": YES\n")

def check(x, y, grid):
	return check_hor(x, y, grid) or check_ver(x, y, grid)

def check_hor(x, y, grid):
	v = grid[x][y]
	return len(filter(lambda l: int(l) > int(v), grid[x])) == 0

def ver(x, y, grid):
	o = []
	for n in grid:
		o.append(n[y])
	return o

def check_ver(x, y, grid):
	v = grid[x][y]
	return len(filter(lambda l: int(l) > int(v), ver(x, y, grid))) == 0

solve("in2")
