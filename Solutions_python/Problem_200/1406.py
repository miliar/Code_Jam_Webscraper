#!/usr/bin/python

import math
import collections

def parseFile(inputPath):
	count = 0
	lines = []
	try:
		with open(inputPath, 'r') as file:
			for line in file.readlines():
				if count==0:
					count += 1
					continue
				
				lines.append(line.replace('\n', ''))
				count += 1

	except:
		print "Failed"

	return lines

def updateNumber(number, end):
#	print "Update number: {} end: {}".format(number, end)
	for i in xrange(0, end+1):
		pos = end - i
		num = int(number[pos])
#		print "i: {} pos: {} Num: {} number: {}".format(i, pos, num, number)
		if num>0:
			number[pos] = str(num-1)
			break
		
		if pos==0:
			break

		number[pos] = '9'
		for j in xrange(pos+1, len(number)):
			number[j] = '9'
		
		number = updateNumber(number, pos-1)
		
		break

	return number

def solve(str):
	number = list(str)
	length = len(number)
	for i in xrange(0, length-1):
		curr = length-i-1
		currNum = int(number[curr])
		prev = length-i-2
		prevNum = int(number[prev])
		if currNum>=prevNum and currNum!=0:
			continue

#		print "compare: {} and {}".format(prevNum, currNum)
		number[curr] = '9'
		for j in xrange(curr+1, len(number)):
			number[j] = '9'
		
		number = updateNumber(number, curr-1)

	return int("".join(number))


#inputPath = "/Users/Non/Documents/Work/CodeJam2017/B/input.in"
#inputPath = "/Users/Non/Documents/Work/CodeJam2017/B/B-small-attempt1.in"
inputPath = "/Users/Non/Documents/Work/CodeJam2017/B/B-large.in"
outputPath = inputPath.replace(".in", ".out")

print "Input: {}".format(inputPath)
print "Output: {}".format(outputPath)

numbers = parseFile(inputPath)
#print numbers

#result = solve("216")
#print "Tidy number: {}".format(result)

try:
	count = 0
	with open(outputPath, 'wb') as file:
		for num in numbers:
			count += 1
			result = solve(num)
#			print "#{} tidy number: {}".format(count, result)
			res = "Case #{}: {}\n".format(count, result)
			file.write(res)
except:
	print "Write output failed"

#	print "Input number: {} last number: {}".format(n, res)
