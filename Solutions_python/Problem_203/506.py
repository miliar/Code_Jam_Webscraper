import sys
import os
import numpy as np
import random


def readFile(filename):
	with open(filename, 'r') as fp:
		T = int(fp.readline())
		output = []
		while True:
			try:
				R, C = [int(x) for x in fp.readline().strip().split(' ')]
			except:
				break
			A = [[''] * C for _ in range(R)]
			for r in range(R):
				row = fp.readline().strip().split(' ')[0]
				for c in range(C):
					A[r][c] = row[c]
			output.append([R,C,A])
		return T, output
				
def solve(A):
	R, C, M = A
	print M
	L = {}
	for r in range(R):
		for c in range(C):
			car = M[r][c]
			if car == '?':
				continue
			if not M[r][c] in L:
				L[car] = [r, r, c, c]
			else:
				l = L[car]
				L[car] = [min(r, l[0]), max(r, l[1]), min(c, l[2]), max(c, l[3])]
	for car in L:
		mr, Mr, mc, Mc = L[car]
		for i in range(mr,Mr+1):
			for j in range(mc,Mc+1):
				M[i][j] = car
		while mr > 0:
			X = M[mr-1][mc:Mc+1]
			if len(X)==len([x for x in X if x=='?']):
				mr = mr-1
				M[mr][mc:Mc+1] = car
			else:
				break
		while Mr < R-1:
			X = M[Mr+1][mc:Mc+1]
			if len(X)==len([x for x in X if x=='?']):
				Mr = Mr+1
				M[Mr][mc:Mc+1] = car
			else:
				break
		while mc > 0:
			X = [M[i][mc-1] for i in  range(mr, Mr+1)]
			if len(X)==len([x for x in X if x=='?']):
				mc = mc-1
				for i in range(mr,Mr+1):
					M[i][mc] = car
			else:
				break
		while Mc < C-1:
			X = [M[i][Mc+1] for i in  range(mr, Mr+1)]
			if len(X)==len([x for x in X if x=='?']):
				Mc = Mc+1
				for i in range(mr,Mr+1):
					M[i][Mc] = car
			else:
				break
	return M
	
	
if __name__ == "__main__":
	input_filename = sys.argv[1]
	T, A = readFile(input_filename)
	fp = open('output.txt', 'w')
	for t in range(T):
		M = solve(A[t])
		R, C, _ = A[t]
		fp.write("Case #{}:\n".format(t+1))
		for r in range(R):
			line = ''.join(M[r])
			fp.write(line)
			fp.write('\n')

	
	






