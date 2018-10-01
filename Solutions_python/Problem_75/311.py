#!/usr/bin/env python
# encoding: utf-8


import sys
import os

def applyCombs(current,combs):
	if len(current) > 1:
		for c in combs:
			if len(current) > 1:
				if set([current[-1],current[-2]]) == set([c[0],c[1]]):
					current.pop()
					current.pop()
					current.append(c[2])
	return current

def applyOpps(current,opps):
	if len(current) > 1:
		for o in opps:
			if o[0] in current and o[1] in current:
				return []
	return current

def solveSingle(combs,opps,invoke):
	final = []
	
	for x in invoke:
		final.append(x)
		final = applyCombs(final,combs)
		final = applyOpps(final,opps)
	
	return final


def main():
	infile = open('B-large.txt','r')
	outfile = open('B-large-answer.txt','w')
	num_tests = int(infile.readline())
	
	for x in range(num_tests):
		lines = infile.readline().split(" ")
		
		num_comb = int(lines.pop(0))
		combs = []
		for y in range(num_comb):
			combs.append(list(lines.pop(0).strip()))
			
		
		num_opps = int(lines.pop(0))
		opps = []
		for y in range(num_opps):
			opps.append(list(lines.pop(0).strip()))
			
		lines.pop(0)
		
		invoke = list(lines.pop(0).strip())
		
		final = solveSingle(combs,opps,invoke)
	
		outfile.write("Case #"+str(x+1)+": ["+", ".join(final)+"]"+"\n")
		print "Case #"+str(x+1)+": ["+", ".join(final)+"]"
	
	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()

