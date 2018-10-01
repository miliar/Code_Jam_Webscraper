#!/usr/bin/env python
import math

inFile = open("B-large.in.txt", 'r')
lineCounter = int(inFile.readline())
c = 1
results = ""
while c <= lineCounter:
	s = inFile.readline()
	cookieList = s.split(' ')
	farmCost = float(cookieList[0])
	farmProduce = float(cookieList[1])
	target = float(cookieList[2])
	totalTime = 0
	currentProduce = 2
	while True:
		if target / currentProduce > farmCost / currentProduce + target / (currentProduce + farmProduce):
			totalTime += farmCost / currentProduce
			currentProduce += farmProduce
		else:
			totalTime += target / currentProduce
			break
	results += "Case #" + str(c) + ": " + str(totalTime) + '\n'
	c += 1
outFile = open("B-large.out.txt", 'w')
outFile.write(results[0:len(results)-1])