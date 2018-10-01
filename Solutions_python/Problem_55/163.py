#!/usr/bin/env python

import sys

def solve(R,K,Groups):
	#load the car full and then iterate
	return solveRec(R,K, 0, Groups, {}, 0)

def solveRec(R, K, offset, Groups, Memory, test):
	if R == 0:
		return 0
	if offset == 0 and 0 in Memory:
		#how many rides did it take to get back here?
		rOld = Memory[offset]
		rDiff = rOld - R
		if rDiff <= R:
			return test * (R / rDiff) + solveRec(R % rDiff,K, offset, Groups, Memory, 0)

	summation = Groups[offset]
	if summation > K:	#group can not fit on coaster, game over
		print "those MF pricks at google"
		return 0
	t = (offset + 1) % len(Groups)
	while t != offset:	#can't put more than the queue on the coaster
		summation += Groups[t]
		if summation > K:
			summation -= Groups[t]
			break
		t += 1
		if t >= len(Groups):
			t = 0
#	print offset, t
	Memory[offset] = R
	return summation + solveRec(R-1, K, t, Groups, Memory, test + summation)

def solveFile(Filename):
	inFile = file(Filename, "r")
	outFile = file(Filename[:-2]+"out", "w")
	foo = int(inFile.readline())
	i = 1
	while i <= foo:
		R, K = map(int, inFile.readline().split(" ")[:2])
		groups = map(int, inFile.readline().split(" "))
		outFile.write("Case #%i: %i\n" %(i, solve(R, K, groups)))
		i += 1

sys.setrecursionlimit(10000)

assert 21 == solve(4,6, [1,4,2,1])	#1+4, 2+1+1, 4+2, 1+1+4 = 5+4+6+6 = 21
assert 100 == solve(100,10, [1])
assert 20 == solve(5,5, [2,4,2,3,4,2,1,2,1,3])
assert 7 == solve(5,10,[1,1,2,3,11])
for i in range(2,20):
	assert 7*i == solve(2*i,4, [2,2,3])
assert 50000 == solve(1000, 100, [4, 3, 9, 1, 2, 5, 6, 9, 1, 10])
assert 1994 == solve(734, 3, [1,2,3,3,2,1,1,2,3,1])

solveFile("/home/king/scripts/python/google codejam/theme park/C-small-attempt3.in")
#solveFile("/home/king/scripts/python/google codejam/temp/C-large.in")

