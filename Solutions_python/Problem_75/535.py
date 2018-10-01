#!/usr/bin/python
# Zoltan Puskas <mr.zoltan.puskas@gmail.com>
# Magicka 

import sys

fin = open('B-large.in', 'r')
fout = open('B-large.out', 'w')

numOfTestCases = int(fin.readline())
testCaseNumber = 0
print "Number of testcases: {}".format(numOfTestCases)

for line in fin:
	testCaseNumber += 1
	elements = []
	opposed = []
	combines = {}
	invocation = ""
	magicLine = line.rstrip().rsplit(' ')
	itemCnt = 0
	if int(magicLine[itemCnt]) > 0:
		for i in range(int(magicLine[itemCnt])):
			combines[magicLine[itemCnt+i+1][:2]] = magicLine[itemCnt+i+1][2]
	itemCnt += int(magicLine[itemCnt]) + 1
	if int(magicLine[itemCnt]) > 0:
		for i in range(int(magicLine[itemCnt])):
			opposed.append(magicLine[itemCnt+i+1])	
	itemCnt += int(magicLine[itemCnt]) + 2
	invocation = magicLine[itemCnt]

	for e in invocation:
		elements.append(e)
		if len(elements) > 1:
			 endItems = ''.join(elements[-2:])
			 endItemsR = ''.join(elements[-2:][::-1])
			 if endItems in combines: 
				 elements.pop()
				 elements.pop()
				 elements.append(combines[endItems])
			 elif endItemsR in combines:
				 elements.pop()
				 elements.pop()
				 elements.append(combines[endItemsR])
			 for opposing in opposed:
				 if opposing[0] in elements and opposing[1] in elements:
					 del elements[:]
	print "Final element list: [{}]".format(', '.join(elements))
	result = "Case #{}: [{}]\n".format(testCaseNumber, ', '.join(elements))    	
	fout.write(result)

