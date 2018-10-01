#!/usr/bin/env python

def sol(S):
	friends = 0
	up = 0
	for k in range(len(S)):
		if k<=up:
			up += S[k]
		elif S[k]>0:
			needed = k-up
			friends += needed
			up += S[k] + needed
	return friends

T = int(raw_input())
for case in range(1,T+1):
	c = raw_input().split()
	Smax = int(c[0])
	S = []
	for k in range(0,Smax+1):
		S.append(int(c[1][k]))
	print('Case #%d: %d' % (case,sol(S)))
