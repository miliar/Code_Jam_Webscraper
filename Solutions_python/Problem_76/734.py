#! /usr/bin/python

import sys
import os
import math

def bfr(Sean, Patrick):
	Sean.sort()
	Patrick.sort()

	fun = lambda x, y: x^y
	sum = lambda x, y: x+y

	if reduce(fun, Sean) != 0:
		return None

	Patrick.append(Sean.pop(0))

	queue = [(Sean, Patrick)]


	while True:
		if len(queue) == 0:
			return None

		queue.sort(key=lambda tup: reduce(sum, tup[1]))

		Sean, Patrick = queue.pop(0)

		if not Sean:
			return None

		if (not Patrick) and (reduce(fun, Sean) == 0):
			return reduce(sum, Sean)


		if Patrick and reduce(fun, Sean) == reduce(fun, Patrick):
			return reduce(sum, Sean)
		else:
			for candy in Sean:
				copySean = Sean[:]
				copyPatrick = Patrick[:]
				copySean.remove(candy)
				copyPatrick.append(candy)
				copyPatrick.sort()
				queue.append((copySean, copyPatrick))




filename = sys.argv[1]
f = open(filename, 'r')

file_string = f.read()
file_string = file_string.split('\n')


T = int(file_string[0])
caseNum = 1

file_string.pop(0)

for case in range(T):
	N = int(file_string.pop(0))
	candies = file_string.pop(0)
	
	candies = candies.split(' ')
	candies = map(int, candies)
	
	candies.sort()

	Sean = candies
	Patrick = []

	result = bfr(Sean, Patrick)
	
	if result == None:
		print_string = 'NO'
	else:
		print_string = str(result)


	print "Case #"+str(caseNum)+": "+print_string
	caseNum += 1



			


