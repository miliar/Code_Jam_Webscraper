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
	
	trans = {'y':'a', 'e':'o', 'q':'z', 'z':'q'}
	revtrans = {}
	goog = """ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"""
	eng = """our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"""  
	
	for i in range(len(goog)):
		trans[goog[i]] = eng[i]
	
	
	infile = open('small1.txt','r').readlines()
	outfile = open('small1output.txt','w')
	results = []
	casenum = 1
	for line in infile[1:]:
		output = ''
		for l in line.strip():
			output += trans[l]
		results.append('Case #%s: %s' % (casenum, output))
		casenum += 1
	print results
	for line in results:
		outfile.write(line)
		outfile.write('\n')	
	
		
	
			
	

	
	
if __name__ == '__main__':
	main()

