#!/usr/bin/env python 

import sys 
import re 
from decimal import *

def eval(list,base):
	total = 0

	for i in range(len(list)):
		total += (list[i] * pow(base,i))

	return(total)	
		

def process():
	
	string = sys.stdin.readline().strip()
	nDigits = len(string)
	hash = {}
	max = 1

	list = []

	#first s always 1 
	hash[string[0]] = 1
	list.append(1)

	current = 0 

	for i in range(1,len(string)):
		try:
			list.append(hash[string[i]])
		except:
			hash[string[i]] = current
			
			if(current == 0):
				current = 2
			else:
				current = current + 1

			list.append(hash[string[i]])
	
		
	#print string
	#print list 		

	base = current
	if(base < 2):
		base = 2
	#print base
	list.reverse()

	xx = eval(list,base)	
	return(xx)
			
		
		


	







if(__name__=="__main__"):
	#getcontext().prec = 7

	nTestCases = int(sys.stdin.readline().strip())
	#nTestCases = 1
	for i in range(1,nTestCases+1):
		number = process()
		print "Case #" + str(i) + ": %d" %number 
	
