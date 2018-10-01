#!/usr/bin/env python

from __future__ import print_function
import copy
import itertools
import sys

def tokenize(f, delim = [ ' ', '\n' ]):
	token = list()

	while True:
		ch = f.read(1)
		if ch == '':
			yield ''.join(token)
			raise StopIteration
			token = list()
		elif ch in delim:
			yield ''.join(token)
			token = list()
		else:
			token.append(ch)

def GetWP(N, M):
	WP = [ 0.0 ] * N
	for r in range(0, N):
		won  = 0
		lost = 0
		for c in range(0, N):
			if M[r][c] == '0':
				lost += 1
			elif M[r][c] == '1':
				won  += 1

		if won > 0:
			WP[r] = won / float(won + lost)
	return WP

def GetOWP(N, M):
	OWP = [ 0.0 ] * N
	for r in range(0, N):
		# find opponents
		opponents = list()
		for c in range(0, N):
			if M[r][c] != '.':
				opponents.append(c)

		# remove self-matches
		Mr = copy.deepcopy(M)
		for c in range(0, N):
			Mr[r][c] = '.'
			Mr[c][r] = '.'

		# calculate WP of opponents
		for opponent in opponents:
			OWP[r] += GetWP(N, Mr)[opponent]
		OWP[r] /= float(len(opponents))
	return OWP

def GetOOWP(N, M):
	OOWP = [ 0.0 ] * N
	for r in range(0, N):
		# find opponents
		ops = list()
		for c in range(0, N):
			if M[r][c] != '.':
				ops.append(c)

		# find opponents' opponents
		for op in ops:
			OOWP[r] += GetOWP(N, M)[op]
		OOWP[r] /= float(len(ops))
	return OOWP

tokens = tokenize(sys.stdin)
T      = int(tokens.next())

for t in range(0, T):
	N = int(tokens.next()) # number of teams
	M = [ [ None for c in range(0, N) ] for r in range(0, N) ]

	# build matrix
	for r in range(0, N):
		row = tokens.next()
		for c in range(0, N):
			M[r][c] = row[c]
	
	WP   = GetWP(N, M)
	OWP  = GetOWP(N, M)
	OOWP = GetOOWP(N, M)
	RPI  = [ 0.0 ] * N

	print('Case #{0}:'.format(t + 1))
	for r in range(0, N):
		RPI[r] = 0.25 * WP[r] + 0.50 * OWP[r] + 0.25 * OOWP[r]
		print(RPI[r])
