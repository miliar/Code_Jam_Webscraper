#!/usr/bin/env python

from __future__ import print_function

import sys

def buildElementList(combineList, opposeList, elementList):
	triggerList = {}
	resultList = []
	resultSize = 0
	
	for element in elementList:
		#if this is first element, insert element
		if (not resultList):
			resultList.append(element)
		else:
			combineCandidate = resultList[-1] + element
			#see if we can combine two letters
			if(combineCandidate in combineList):
				resultList[-1] = combineList[combineCandidate]
			#see if this character has an opposing character
			elif ((element in opposeList) and (opposeList[element] in resultList)):
				resultList = []
			else:
				resultList.append(element)
				
	return resultList
	
def buildInputList(inputString):
	inputList = inputString.split()
	
	combineList = {}
	opposeList = {}
	elementList = []
	
	numCombineElements = int(inputList[0])
	combineElements = inputList[1:numCombineElements+1]
	
	for i in combineElements:
		combineList[i[0:2]] = i[-1]
		combineList[i[1::-1]] = i[-1]
	
	numOpposeElements = int(inputList[numCombineElements+1])
	opposeElements = inputList[numCombineElements+2:numCombineElements+numOpposeElements+2]
	
	for i in opposeElements:
		opposeList[i[0]] = i[1]
		opposeList[i[1]] = i[0]
	
	elementList = list(inputList[-1])
	
	return (combineList, opposeList, elementList)
	
	

if __name__ == "__main__":

	if(len(sys.argv) != 3):
		print("Usage: %s inputfile outputfile" % sys.argv[0], file=sys.stderr)
		sys.exit(1)
		
	inputFile = open(sys.argv[1])
	outputFile = open(sys.argv[2], "w")
	
	numTestCases = int(inputFile.readline())
	
	for i in range(1, numTestCases+1):
		elementList = buildElementList(*buildInputList(inputFile.readline()))
		outputFile.write("Case #%d: [" % i);

		if(elementList):
			for j in elementList[:-1]:
				outputFile.write("%s, " % j);
			
			outputFile.write("%s" % elementList[-1])
		
		outputFile.write("]\n")
		
	inputFile.close();
	outputFile.close();
		