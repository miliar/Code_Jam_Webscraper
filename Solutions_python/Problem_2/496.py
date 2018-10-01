#!/usr/bin/env python2.3
#
#  codejamtrain.py
#  
#
#  Created by HaoQi Li on 7/17/08.
#  Copyright (c) 2008 __MyCompanyName__. All rights reserved.
#

f = open('B-small-attempt4.txt')
casemax = int( f.readline())
out=open("B-small-an.txt", "w")

#Big loop of cases
for x in range(casemax):

	#get info
	turntime = int ( f.readline() )
	nanbStringTemp = f.readline()
	nanbString = nanbStringTemp.split()
	na = int(nanbString[0])
	nb = int(nanbString[1])
	liAgo = []  #int lists
	liAstay = []
	liBgo = []
	liBstay = []
	numStarA=0
	numStarB=0
	#get the na time
	for a in range(na):
		linestrTemp = f.readline()
		linestr = linestrTemp.replace(":","").split()
		liAgo.append(int(linestr[0]))
		liBstay.append(int(linestr[1])+turntime)
	#get the nb time
	for b in range(nb):
		linestrTemp = f.readline()
		linestr = linestrTemp.replace(":","").split()
		liBgo.append(int(linestr[0]))
		liAstay.append(int(linestr[1])+turntime)
		
	#sort lists
	liAgo.sort()
	liAstay.sort()
	liBgo.sort()
	liBstay.sort()
	
	##out.write(str(liAgo)+"\n")
	#out.write(str(liAstay)+"\n")
	#out.write(str(liBgo)+"\n")
	#out.write(str(liBstay)+"\n")
	
	#figure out number start at A
	for i in range(len(liAgo)):
		if (liAstay) and liAgo[i] < liAstay[0]:
			numStarA+=1
			#out.write(str(i) + " liAgo "+str(liAgo[i])+" liAstay "+str(liAstay[0])+" numSA " + str(numStarA) + "\n")
		elif (liAstay):
			liAstay.pop(0)
		else:
			numStarA+=1
			
	#	if (liAstay) and (liAgo[i] >= liAstay[0]):
	#		liAstay.pop(0)
	#	else:
	#		numStarA+=1
	
	#figure out number start at B
	for i in range(len(liBgo)):
		if (liBstay) and liBgo[i] < liBstay[0]:
			numStarB+=1
			#out.write(str(i) + " liAgo "+str(liAgo[i])+" liAstay "+str(liAstay[0])+" numSA " + str(numStarA) + "\n")
		elif (liBstay):
			liBstay.pop(0)
		else:
			numStarB+=1	
	#output
	out.write("Case #"+str(x+1)+": "+str(numStarA)+" "+str(numStarB)+"\n")
	#out.write(str(test)+"\n\n")
	#out.write()