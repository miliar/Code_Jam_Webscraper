from math import sqrt, pow, log, ceil, log10, pi
from sys import stdin
import random, math

dic = {}
debug = False

def solve(N, K, R, H):
	if debug:
		print R, H
	M = [(0, 0, 0)] * N
	for j in range(N):
		M[j] = (2 * R[j] * H[j], j, R[j])
	M.sort()
	M.reverse()
	if debug:
		print M
	first = 0
	for i in range(K-1):
		(u, v, w) = M[i]
		first += u

	best = 0
	for i in range(N):
		a = 0
		# take i
		a = R[i] * R[i]	
		if debug:
			print ">", i, a
		nb = 0
		haveI = 0
		j = 0

		# take the best one's, not i
		while (nb < K - 1) and (j < N):
			(u, v, w) = M[j]
			if v == i:
				haveI = 1
			if w <= R[i]:
				nb += 1
				a += u
			j += 1

		if nb == K - 1:
			if haveI == 1:
				# Add another one
				while (nb < K) and (j < N):
					(u, v, w) = M[j]
					if w <= R[i]:
						nb += 1
						a += u
					j += 1

			else:
				# Add i-th
				a += 2 * R[i] * H[i]
				nb += 1

			if a > best and nb == K:
				best = a
			if debug:
				print "->", i, a, p, a * pi			

	print "%.10f" % (math.pi * best)

T = int(stdin.readline())

for i in range(1,T+1):

	N, K = map(int, stdin.readline().split())
	R = [0] * N
	H = [0] * N

	for j in range(N):
		R[j], H[j] = map(int, stdin.readline().split())

	print "Case #" + str(i) + ":", 

	solve(N, K, R, H)