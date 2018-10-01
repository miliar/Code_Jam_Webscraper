#! /usr/bin/env python

import sys

try:
	import psyco
	psyco.full()
except ImportError:
	pass

def case(infile):
	P, K, L = [int(i) for i in infile.readline().strip().split()]
	#print P,K,L
	freq = [int(i) for i in infile.readline().strip().split()]
	#print freq
	sortedletters = range(L)
	sortedletters.sort(key=lambda l:freq[l], reverse=True)
	#print sortedletters
	lettertimes = {}
	i=-1
	#print L/K
	for i in range(L/K):
		#print i
		for letter in sortedletters[i*K:(i+1)*K]:
			lettertimes[letter] = i+1
	#print type(i), i
	for letter in sortedletters[(i+1)*K:]:
		lettertimes[letter] = i+2
	#print lettertimes
	keypresses = [freq[i]*lettertimes[i] for i in range(L)]
	out = sum(keypresses)
	return out
	
if __name__ == '__main__':
	infile = sys.stdin
	infile = open('A-large.in')
	N = int(infile.readline())
	for casenum in xrange(N):
		output = case(infile)
		print 'Case #%d: %d' %(casenum+1, output)

