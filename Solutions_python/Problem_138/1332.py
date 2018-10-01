#!/usr/bin/python
# -*- coding: utf-8 -*-

def line_to_floats(l):
	lfloat = []
	for e in l:
		lfloat.append(float(e))
	return sorted(lfloat)

def win_all(nblocks,kblocks):
	for i in range(len(kblocks)):
		if kblocks[i]>nblocks[i]:
			return False
	return True


def optimal_war(nblocks,kblocks):
	score = 0
	while len(kblocks)>0:
		N = len(kblocks)
		nc = 0
		kc = 0
		while nblocks[nc]>kblocks[kc]:
			if kc==N-1:
				kc = 0
				break
			kc = kc+1
		told = nblocks[nc]
		# print "Naomi tells %.7fkg (real %.5fkg), Ken plays %.5f"%(told,nblocks[nc],kblocks[kc])
		if nblocks[nc]>kblocks[kc]:
			score=score+1
			# print score
		kblocks.pop(kc)
		nblocks.pop(nc)
	return score


def optimal_dwar(nblocks,kblocks):
	dw 		= 0.0000001
	score 	= 0
	while len(kblocks)>0:
		N = len(kblocks)
		if not win_all(nblocks,kblocks): # Naomi looses, cannot win against this one
			kc = N-1
			nc = 0
			told = kblocks[kc]-dw
		else:
			nc = 0
			kc = 0
			told = nblocks[nc]
			score = score+1
		# print "Naomi tells %.7fkg (real %.5fkg), Ken plays %.5f"%(told,nblocks[nc],kblocks[kc])
		kblocks.pop(kc)
		nblocks.pop(nc)
	return score


def main():
	# filestr = 'D-small-attempt0'
	filestr = 'D-large'
	# filestr = 'D-verysmall'
	fin = open(filestr+'.in','r')
	fout = open(filestr+'.out','w')

	lines = fin.read().splitlines()
	T = int(lines[0])
	for i in range(T):
		N = int(lines[1+3*i])
		naomi_blocks 	= line_to_floats(lines[2+3*i].split(' '))
		ken_blocks 		= line_to_floats(lines[3+3*i].split(' '))
		
		dwar_score 	= optimal_dwar(naomi_blocks[:],ken_blocks[:])
		war_score 	= optimal_war(naomi_blocks,ken_blocks)

		str=  'Case #%d: %d %d\n'%(i+1,dwar_score,war_score)
		fout.write(str)
		print str

	fin.close()
	fout.close()


if __name__ == "__main__":
    main()
