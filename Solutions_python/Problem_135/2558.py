#!/usr/bin/env python3

import sys

def solve(res1, grid1, res2, grid2):
	inter = set(grid1[res1]) & set(grid2[res2])
	if not inter:
		return "Volunteer cheated!"
	if len(inter) > 1:
		return "Bad magician!"
	return inter.pop()

def read_input():
	result1 = int(sys.stdin.readline()) - 1
	grid1 = [[int(x) for x in sys.stdin.readline().split()] for _ in range(4)]
	result2 = int(sys.stdin.readline()) - 1
	grid2 = [[int(x) for x in sys.stdin.readline().split()] for _ in range(4)]
	return result1, grid1, result2, grid2

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for i in range(ncases):
		result = solve(*read_input())
		print('Case #', i + 1, ': ', result, sep='')
