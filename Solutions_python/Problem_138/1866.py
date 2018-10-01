#!/usr/bin/env python

from sys import argv

def war(nBlocks, n_blocks, k_blocks):
	''' returns the number of points Naomi wins in regular war if Ken plays optimally.

		accepts: int, list, list
		returns: int
	'''
	n = 0
	k = 0
	while True:
		if k >= nBlocks:
			break
		if k_blocks[k] > n_blocks[n]:
			n += 1
		k += 1
	return nBlocks - n

def deceitful_war(nBlocks, n_blocks, k_blocks):
	''' returns the number of points Naomi wins if she plays deceitful war optimally while Ken plays
	    regular war optimally.

	    accepts: int, list, list
	    returns: int
	'''
	n = 0
	k = 0
	while True:
		if n >= nBlocks:
			break
		if n_blocks[n] > k_blocks[k]:
			k += 1
		n += 1
	return k
	
	'''while True:
		if len(n_blocks) == 0:
				return 0
		if n_blocks[0] > k_blocks[-1]:
			return len(n_blocks)
		else:
			n_blocks.pop(0)
			k_blocks.pop(-1)'''


ansStr = "Case #%d: %d %d"
out = []
with open(argv[1]) as f_in:
	nCases = int(f_in.next())
	for case in xrange(nCases):
		nBlocks = int(f_in.next())
		naomi = map(float, f_in.next().split())
		ken = map(float, f_in.next().split())
		naomi.sort()
		ken.sort()
		# calculate both scores
		war_score = war(nBlocks, naomi, ken)
		deceitful_war_score = deceitful_war(nBlocks, naomi, ken)
		out.append(ansStr % (case+1, deceitful_war_score, war_score))

with open('deceitful_war.out', 'w') as f_out:
	for s in out:
		f_out.write(s+"\n")