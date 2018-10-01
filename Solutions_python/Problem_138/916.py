#!/usr/bin/python

import sys

def kenMove(naomiTold,ken):
	candidate = 1.0
	for piece in ken:
		if (piece > naomiTold) and (piece < candidate):
			candidate=piece
	if candidate == 1.0:
		return min(ken)
	return candidate

def siguientea(superar,naomi2):
	candidato = 1.0
	for item in naomi2:
		if (item>superar) and (item<candidato):
			candidato=item

	return candidato

def deceifulSelect(naomi2,ken2):
	if (max(naomi2)>max(ken2)):
		return max(ken2)+0.000001,siguientea(min(ken2),naomi2)#la siguiente que gane a la mas pequena de ken

	return max(ken2)-0.000001,min(naomi2)

def processCase(naomi,ken):
	# *** BEGIN CODE PROCESSING CASE ***

	naomi2=list(naomi)
	ken2=list(ken)

	kscore=0
	nscore=0
	lon = len(naomi)

	for i in xrange(0,lon):
		trozo = naomi.pop()
		km=kenMove(trozo,ken)

		if km > trozo:
			kscore = kscore+1
		else:
			nscore = nscore+1

		ken.remove(km)

	# alternative war
	kscore2=0
	nscore2=0
	for i in xrange(0,lon):
		nm,played=deceifulSelect(naomi2,ken2)
		km=kenMove(nm,ken2)

		#print "naomi says "+str(nm)+" plays "+str(played)+ " vs ken's "+str(km)

		if km > nm:
			kscore2 = kscore2+1
		else:
			nscore2 = nscore2+1

		ken2.remove(km)
		naomi2.remove(played)

	# *** END CODE PROCESSING CASE ***
	return nscore2,nscore

def readCase(case):

	# *** BEGIN CODE READING CASE ***
	caseInput=sys.stdin.readline()
	naomitxt=sys.stdin.readline()
	kentxt=sys.stdin.readline()

	naomi=map(float,naomitxt.split())
	ken=map(float,kentxt.split())

	# *** END CODE READING CASE ***

	solution1,solution2=processCase(naomi,ken)
	print "Case #"+str(case)+": "+str(solution1)+" "+str(solution2)

cases=int(sys.stdin.readline())

for case in range(cases):
	readCase(case+1)

