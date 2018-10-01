#!/usr/bin/env python

import sys

def main():
	with open(sys.argv[1]) as f:
		solve(f)

def solve(f):
	lines = f.readlines()
	T = int(lines[0])
	b = 1
	for i in range(1, T+1):
		M, N = map(int, lines[b].split())
		grid = []
		for l in range(b+1, b+M+1):
			grid.append(hex_to_binary(lines[l].strip()))
		b += M+1
		answer = solve_real(grid, M, N)
		print "Case #%d: %s" % (i, len(answer))
		for a in answer:
			print a[0], a[1]

def solve_real(grid, M, N):
	q = min(M, N)
	r = []

	while q:
		c = find_grids_of_size(grid, M, N, q)
		if c:
			r.append((q, c))
		q -= 1

	return r

def find_grids_of_size(grid, M, N, size):
	c = 0
	for i in range(M - size + 1):
		for j in range(N - size + 1):
			if is_grid_of_size(grid, i, j, size):
				c += 1

				for x in range(i, i+size):
					for y in range(j, j+size):
						grid[x][y] = -100

	return c

def is_grid_of_size(grid, i, j, size):
	if size == 1:
		return grid[i][j] != -100

	for x in range(i, i+size):
		if grid[x][j+size-1] != 1 - grid[x][j+size-2]:
			return False

	for y in range(j, j+size):
		if grid[i+size-1][y] != 1 - grid[i+size-2][y]:
			return False

	return is_grid_of_size(grid, i, j, size-1)

def hex_to_binary(s):
	r = []
	l = len(s)
	i = int(s, 16)
	while i:
		r.append(i % 2)
		i = i >> 1
	while len(r) < l*4:
		r.append(0)
	r.reverse()
	return r

if __name__ == '__main__':
	main()