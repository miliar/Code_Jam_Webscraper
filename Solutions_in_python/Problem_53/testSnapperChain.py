#
#  testSnapperChainr.py
#  
#
#  Created by FEI LIU on 5/8/10.
#  Copyright (c) 2010 ucla. All rights reserved.
#

from SnapperChain_1 import snapperChain 

input = open('A-small-attempt0.in', 'r')
ouput = open('data_result_small', 'w')
caseNumber = 0
firstLine = 1
#lineNo = 1
for line in input.readlines():
	if(firstLine):
		caseTotal = line.rstrip()
		firstLine = 0
		continue
#	lineNo += 1
	line = line.rstrip()
#	if(lineNo%2 == 0):
#		parts = map(int, line.split(" "))
#		R = parts[0]
#		k = parts[1]
#		N = parts[2]
#		caseNumber += 1
#		continue
	caseNumber += 1	
	gList = map(int, line.split(" "))
	N = gList[0]
	K = gList[1]
	lightState = snapperChain(N, K)
	if(lightState == 0):
		rstStr = "OFF"
	else:
		rstStr = "ON"

	ouput.write("Case #")
	ouput.write(str(caseNumber))
	ouput.write(":" + " " + rstStr + "\n")	

input.close()
ouput.close()	
