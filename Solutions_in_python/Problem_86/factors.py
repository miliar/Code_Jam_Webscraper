#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Shafeen Tejani on 2011-05-22.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import math


def findNotes2(lowest,highest,otherNotes):
	
	for i in range(lowest,highest+1):
		if (inHarmonyWith(i,otherNotes)):
			return i
	
	return "NO"


def findNotes(lowest,highest,otherNotes):
	
	if lowest <= 1: return 1
	
	maxNum = max(otherNotes)
	
	maxFactors = factors(max(otherNotes))
	
	
	othersInHarmony = True
	notInHarmony = []
	
	#check that other notes are in harmony
	for i in otherNotes:
		if not (i in maxFactors):
			notInHarmony.append(i)
			othersInHarmony = False

	if othersInHarmony:
		#if in range return
		for i in maxFactors:
			if (i >= lowest and i <= highest):
				if inHarmonyWith(i,otherNotes):
					return i
	
		start = maxNum
		while start <= highest:
			if start >= lowest:
				return start
			start += maxNum
	
		return "NO"
	
	else:
		#lowestNIH = min(notInHarmony)
		start = max([maxNum,lowest])
		
		while (not isMultiple(start,notInHarmony,maxNum)) and (start <= highest):
			start += 1
		
		if start <= highest:
			return start
		else:
			return "NO"


def inHarmonyWith(i,notes):
	
	for n in notes:
		if (n%i != 0 and i%n != 0): return False
	
	return True

def isMultiple(check, listOfVals, maxNum):
	if check%maxNum != 0: return False
	
	for i in listOfVals:
		if check%i != 0: return False
		
	return True 


def factors(n):  
    fact=[1,n]  
    check=2  
    rootn=math.sqrt(n)  
    while check<rootn:  
        if n%check==0:  
            fact.append(check)  
            fact.append(n/check)  
        check+=1  
    if rootn==check:  
        fact.append(check)  
    
    fact.sort()
    return fact

def main():
	infile = open('C-small.txt','r')
	outfile = open('C-small-answer.txt','w')
	
	num_tests = int(infile.readline())

	for x in range(num_tests):
		nums = infile.readline().split()
		nums = [long(n.strip()) for n in nums]
		freqs = nums[0]
		lowest = nums[1]
		highest = nums[2]
		notes = infile.readline().split()
		notes = [long(n.strip()) for n in notes]
		
		answer = findNotes2(lowest,highest,notes)
		
		print "Case #"+str(x+1)+":",answer
		outfile.write("Case #"+str(x+1)+": "+str(answer)+"\n")

	
	infile.close()
	outfile.close()


if __name__ == '__main__':
	main()

