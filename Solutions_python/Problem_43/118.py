#!/usr/bin/env python2.6
'''
Created on 03/set/2009

@author: marco
'''
import sys
import re


if __name__ == '__main__':
	mainL=[]
	
	inp = open(sys.argv[1], 'r')
	out = open(sys.argv[2], 'w')
	
	line = inp.readline().rstrip("\n")
	T=int(line)
	for i in range(T):
		out.write("Case #%d: "%(i+1))
		myDict={}
		mySt=[]
		line = inp.readline().rstrip("\n")
		myDict[line[0]]=1
		lastInt=0
		c=1
		while (lastInt==0 and c<(len(line)-1)):
			if(not myDict.has_key(line[c])):
				myDict[line[c]]=0
				lastInt=2
			c+=1			
	
		for c in line:
			if(not myDict.has_key(c)):
				myDict[c]=lastInt
				lastInt+=1
			mySt.append(myDict[c])

		base=len(myDict)
		if(base<2):
			base=2
		retval=0
		for j in range(len(mySt)):
			retval+=pow(base, j)*mySt[len(mySt)-1-j]
		out.write("%d\n"%retval)
			
	
	

