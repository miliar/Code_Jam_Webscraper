#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Haley Proctor on 2012-04-14.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	prob1()
	pass



def prob1():
	
	infile = open('small2.txt','r').readlines()
	outfile = open('small2output.txt','w')
	results = []
	casenum = 1
	
	for line in infile[1:]:
		output = ''
		surprises =0
		non = 0
		
		case = line.strip().split()
		dancers = int(case[0])
		surprise = int(case[1])
		cutoff = int(case[2])
		scores = [int(i) for i in case[3:]]
		
		print scores
		for i in scores:
			print i,
			if i >= 3 * cutoff - 2:
				non += 1
				print 'OK'
			elif i >= 3 * cutoff - 4 and i > cutoff:
				surprises += 1
				print 'Sur'
			else:
				print 'Not OK'
	
		results.append('Case #%s: %s' % (casenum, non + min(surprises, surprise)))
		casenum += 1
		print case, non, surprises, results[-1]
	print results
	for line in results:
		outfile.write(line)
		outfile.write('\n')	
	
		
	
			
	

	
	
if __name__ == '__main__':
	main()

