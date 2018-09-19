#
#  testSnapperChainr.py
#  
#
#  Created by FEI LIU on 5/8/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

from r2 import r2 

input = open('A-large.in.txt', 'r')
ouput = open('data_result_s', 'w')
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
		#parts= line.split(" ")
		#oSize = int(parts[0])
		#nSize = int(parts[1])
		inSize = int(line)
		print inSize
		#oldDirList = []
		#newDirList = []
		inList = []
		idx = 0
		caseNumber += 1
		caseBegin = 0
		continue
	
	if(idx < inSize):
		line = line.rstrip()
		inList.append(line)
		idx += 1
	
	if(idx == inSize):
		caseBegin = 1
		mkNo = r2(inList, inSize)
		ouput.write("Case #")
		ouput.write(str(caseNumber))
		ouput.write(":" + " " + str(mkNo) + "\n")	

input.close()
ouput.close()	
