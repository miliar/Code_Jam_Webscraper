#!/usr/bin/env python
# encoding: utf-8
"""
problemB.py

Created by Jesse Krijthe on 2008-07-18.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main(lf, P, K, L):
	
	if P*K<L:
		return 'impossible'
	for g in range(len(lf)):
		lf[g]=int(lf[g])
	
	lf.sort()
	lf.reverse()
	
	minnumber=0
	for i in range (1,P+1):
		for j in range(1,K+1):
			if len(lf)==0:
				break
			minnumber=minnumber+i*lf[0]
			lf.remove(lf[0])
	
	print minnumber
	return minnumber


if __name__ == '__main__':
	fileHandle = open('largeA.in')
	fileOut=open('outputA','w')
	N = int(fileHandle.readline())	
	for i in range(N):
		c=fileHandle.readline().split(' ')
		lf=fileHandle.readline().split(' ')
		rt=main(P=int(c[0]), K=int(c[1]), L=int(c[2]), lf=lf)
		fileOut.write("Case #"+str(i+1)+": "+str(rt)+"\n")
	fileHandle.close()
	fileOut.close()

