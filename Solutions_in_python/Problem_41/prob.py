#!/usr/bin/env python
import sys
from myMod import getNext

FI=open(sys.argv[1],'r')
def readInts():
	return ([int(x) for x in FI.readline().rstrip().split()])

NCases = int(FI.readline())
for nc in range(NCases):
	#process case
	#num=getNext(int(FI.readline()))
	print "Case #"+str(nc+1)+": "+getNext(int(FI.readline()))

















FI.close()

