#!/usr/bin/python

import sys
import math

def equal(a,b):
	return math.fabs(a-b) <= 0.000001

def solve(N,V,X,R,C):
	if N == 1:
		if equal(C[0] , X):
			return V / R[0]
		else:
			return "IMPOSSIBLE"

	if N == 2:
		if C[0] > C[1]:
			temp = C[1] 
			C[1] = C[0]
			C[0] = temp
			temp = R[1]
			R[1] = R[0]
			R[0] = temp

		if X < C[0] or X > C[1]:
			return "IMPOSSIBLE"
		elif X == C[0]:
			return V / (R[0] + (R[1] if C[1] == X else 0.))
		elif X == C[1]:
			return V / R[1]
		else:
			l1 = R[0] * (X-C[0])/((C[1]-X)*R[1])
			if l1 <= 1:
				return V / (R[0] + R[1]*l1)
			else:
				return V / (R[0] / l1 + R[1])
	
	return 0.

if __name__ == "__main__":
	T = int(sys.stdin.readline())

	for t in range(T):
		#N = int(sys.stdin.readline())
		N,V,X = map(float, sys.stdin.readline().split())
		N = int(N)
		R = []
		C = []
		for r in range(N):
			Ri, Ci = map(float, sys.stdin.readline().split())
			R.append(Ri)
			C.append(Ci)
		#keyboard = sys.stdin.readline().split()[0]
		print "Case #{}: {}".format(t+1, solve(N,V,X,R,C))