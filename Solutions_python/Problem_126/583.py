import sys
import os
import string
import re

HELP='\n\
Usage:  \n\
Synopthis: python p.prog  \n\
'

if '-h' in sys.argv:
	print HELP
	sys.exit()



def solve(s, n):
	# find next consonant and previous consonant
	next = {}
	prev = {}
	first = 0 # idx of first consonant

	L = len(s)
	prv = None
	curr = None
	for i in range(L):
		if s[i] not in 'aeiou':
			if first == None:
				first = i
			if prv == None:
				prv = i
			elif curr == None:
				curr = i
				next[prv] = i
				prev[i] = prv
			else:
				prv = curr
				curr = i
				next[prv] = i
				prev[i] = prv
	print next
	print prev				


	# for each segment of n cosonants, move its endpoints without adding/removing cosonants, count the numbers 
	nval = 0
	ncon = 1
	left = first
	right = first

	# find first segment
	done = False
	while ncon < n:
		if right not in next:
			done = True
			break
		else:
			right = next[right]
			ncon += 1
		if ncon == n:
			break
	if done:
		return nval


	while True:
		# compute variations
		print '>>> ', left, right, ncon
		left0 = 0 # number of continuous vowels left to pos left
		if left in prev:
			left0 = left - prev[left] - 1
		# left1 = 0 # number of continuous vowels right to pos left
		# if left in next:
		# 	left1 = next[left] - left - 1
		# right0 = 0
		# if right in prev:
		# 	right0 = right - prev[right] - 1
		right1 = 0
		if right in next:
			right1 = next[right] - right - 1
		# print 'lr:', left0, left1, right0, right1
		# nval += (left0 + 1 + left1) * (right0 + 1 + right1)
		nval += (left0 + 1) * (1 + right1)

		# find next segment
		if right not in next:
			break
		else:
			right = next[right]
			left = next[left]
	return nval
  


def solve2(s, n):
	L = len(s)
	A = [0] * L # A[i] is number of cons in s[0...i]
	A[0] = s[0] not in 'aeiou'
	for i in range(1,L):
		if s[i] not in 'aeiou':
			A[i] = A[i-1]+1
		else:
			A[i] = A[i-1]
	print A

	nval = 0
	for i in range(L):
		for j in range(L):
			if i>j:
				continue
			if A[j] - A[i] + int(s[i] not in 'aeiou') >= n:
				print i,j
				nval += 1

	return nval

def solve3(s,n):
	L = len(s)
	C = [0] * L # C[i] is number of consecutive cons from s[i] if i is a starting cons, else 0

	curr = 0
	done = False
	while curr < L:
		# find next cons
		while s[curr] in 'aeiou':
			curr += 1
			if curr >= L:
				done = True
				break
		if done:
			break

		# find consecutive cons
		i = curr + 1
		while i < L and s[i] not in 'aeiou':
			i += 1
		C[curr] = i-curr

		curr = i
	print C


	 
	# nval = 0
	# # find next segment of >=n consecutive cons
	# i = 0
	# while i < L:
	# 	if C[i] >= n:
	# 		print '>>>', i, C[i]
	# 		nval += (i+1) * (L - (i + C[i] - 1))
	# 		i += C[i] + 1
	# 	else:
	# 		i += 1


	return nval

def solve4(s,n):
	L = len(s)
	nval = 0
	for i in range(L):
		for j in range(i,L):
			nmax = 0
			ncon = 0
			for k in range(i,j+1):
				if s[k] not in 'aeiou':
					ncon += 1
					nmax = max(nmax, ncon)
				else:
					ncon = 0
			if nmax >= n:
				nval += 1
	return nval


if __name__ == '__main__':
	
	T = int(sys.stdin.readline())	
	for i in range(T):
		w,n = sys.stdin.readline().split() 
		n = int(n)
		# print w,n
		print 'Case #'+str(i+1)+': '+str(solve4(w,n))

