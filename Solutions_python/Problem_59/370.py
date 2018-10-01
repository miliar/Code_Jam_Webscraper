#
#  testSnapperChainr.py
#  
#
#  Created by FEI LIU on 5/8/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

from r1 import ffit

input = open('A-large.in.txt', 'r')
ouput = open('data_result_ll', 'w')
caseNumber = 0
firstLine = 1
caseBegin = 1
#lineNo = 1
for line in input.readlines():
	if(firstLine):
		caseTotal = line.rstrip()
		firstLine = 0
		continue	
#	lineNo += 1
	if(caseBegin):
		line = line.rstrip()
		parts= line.split(" ")
		oSize = int(parts[0])
		nSize = int(parts[1])
		oldDirList = []
		newDirList = []
		idx = 0
		caseNumber += 1
		caseBegin = 0
		continue
	
	if(idx < oSize):
		line = line.rstrip()
		oldDirList.append(line)
		idx += 1
	else:
		if(idx >= oSize and idx < nSize + oSize):
			line = line.rstrip()
			newDirList.append(line)
			idx += 1
		
		if(idx == nSize + oSize):
			caseBegin = 1
			mkNo = ffit(newDirList, nSize, oldDirList, oSize)
			ouput.write("Case #")
			ouput.write(str(caseNumber))
			ouput.write(":" + " " + str(mkNo) + "\n")	

input.close()
ouput.close()	
