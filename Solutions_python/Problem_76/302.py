#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Shafeen Tejani on 2011-05-07.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import itertools

def processRow(candies):
	curr = 0
	for x in candies:
		curr = curr ^ x
	
	if curr == 0:
		return sum(candies) - min(candies)
	else:
		return "NO"


def main():
	infile = open('C-large.txt','r')
	outfile = open('C-large-answer.txt','w')
	num_tests = int(infile.readline())

	for x in range(num_tests):
		size = int(infile.readline())
		candies = infile.readline().split()
		candies = [int(c.strip()) for c in candies]
		
		answer = processRow(candies)
		
		print "Case #"+str(x+1)+":",answer
		outfile.write("Case #"+str(x+1)+": "+str(answer)+"\n")
		
	infile.close()
	outfile.close()

if __name__ == '__main__':
	main()

