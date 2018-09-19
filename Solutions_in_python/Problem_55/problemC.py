#!/usr/bin/env python
# encoding: utf-8
"""
problemC.py

Created by Marcel Caraciolo on 2010-05-07.
Copyright (c) 2010 Marcel Caraciolo. All rights reserved.
"""

import sys
import os


def main():
	
	lines = [  line.strip()  for line in open('c-smallIN2.txt')]
	#TestCases
	T = int(lines[0])
	if  T > 50 or T < 1:
		exit()
	l = 1
	T = T * 2
	
	otF = open('C-small.out','w')
	
	number = 1
	while l <= T:
		#GET THE ROLLERCOASTER FEATURES
		R,K,N= map(int,lines[l].split(' '))
		if R > 1000 or R < 1:
			exit()
		if K > 100 or K < 1:
			exit()
		if N > 10 or N < 1:
			exit()
		#print R,K,N
		#GET THE LINE FEATURES
		groups = map(int,lines[l+1].split(' '))
		if len(groups) != N:
			exit()
		#print groups
		l+=2
		
		#Solve the problem
		totalPrice = 0

		while R > 0:
			roller = []
			p = 0
			while sum(roller) <= K and p < len(groups):
				roller.append(groups[p])
				p+=1
			if sum(roller) > K:
				roller = roller[:-1]
			groups = groups[len(roller):]
			#print roller
			totalPrice+= sum(roller)
			groups.extend(roller)
			R-=1
		otF.write('Case #%d: %d\n' %(number,totalPrice))
		number+=1
	
	otF.close()	
				
if __name__ == '__main__':
	main()

