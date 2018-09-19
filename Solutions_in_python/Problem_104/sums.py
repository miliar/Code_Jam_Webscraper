#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import sys
 
testcases = input()
 
def line2intlist(line):
	list = line.split(' ')
	numbers = [ int(x) for x in list ]
	return numbers
 
def getEqual(ints):
	listOfSets = []
	for m in xrange(1, len(ints)):
		listOfSets.extend(set(itertools.combinations(ints, m)))
	listOfSums = []
	for key, el in enumerate(listOfSets):
		sum = 0
		for a in el:
			sum += a
		if sum in listOfSums:
			return [el, listOfSets[listOfSums.index(sum)]]
		else:
			listOfSums.append(sum)
	return -1
 
for i in xrange(0, testcases):
	ints = line2intlist(raw_input())[1:]
	sums = getEqual(ints)
	print("Case #%i:" % (i+1))
	for sublist in sums:
		i = 0
		for el in sublist:
			if i != 0:
				sys.stdout.write(" ")
			sys.stdout.write(str(el))
			i+=1
		print("")
	print("")
