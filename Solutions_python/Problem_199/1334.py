#!/usr/bin/python

import math
import collections

Tuple = collections.namedtuple('Tuple', ['S', 'K'])

def parseFile(inputPath):
	count = 0
	lines = []
	try:
		with open(inputPath, 'r') as file:
			for line in file.readlines():
				if count==0:
					count += 1
					continue
			
				part = line.split()
				tmp = Tuple(part[0], int(part[1]))
				lines.append(tmp)
				count += 1

	except:
		print "Failed"

	return lines

def solve(tuple):
	k = list(tuple[0])
	s = tuple[1]
	length = len(k)
	if length<s:
		return -1
	
	count = 0
	for i in xrange(0, (length-s+1)):
		if k[i]=='+':
			continue
		
		# Flip s times
		k[i] = '+'
		for j in xrange(1, s):
			if k[i+j]=='-':
				k[i+j] = '+'
			else:
				k[i+j] = '-'

		count += 1 # Count Flip time

	for i in xrange(length-s, length):
		if k[i]=='-':
			return -1

	return count

#inputPath = "/Users/Non/Documents/Work/CodeJam2017/A/input.in"
#inputPath = "/Users/Non/Documents/Work/CodeJam2017/A/A-small-attempt0.in"
inputPath = "/Users/Non/Documents/Work/CodeJam2017/A/A-large.in"
outputPath = inputPath.replace(".in", ".out")

print "Input: {}".format(inputPath)
print "Output: {}".format(outputPath)

lines = parseFile(inputPath)
#print numbers

#line = Tuple('---+-++-', 3)
#flip = solve(line)
#print "flip: {}".format(flip)

try:
	count = 0
	with open(outputPath, 'wb') as file:
		for line in lines:
			count += 1
			flip = solve(line)
#			print "#{} flip time: {}".format(count, flip)
			if (flip<0):
				res = "Case #{}: IMPOSSIBLE\n".format(count)
			else:
				res = "Case #{}: {}\n".format(count, flip)

			file.write(res)
except:
	print "Write output failed"

#	print "Input number: {} last number: {}".format(n, res)
