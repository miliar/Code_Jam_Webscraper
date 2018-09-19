#!/usr/bin/env python
# encoding: utf-8
"""
CODEJAM TEMPLATE

Created by Jamie Smith


"""

import sys
import os
from numpy import *
	
def readints(f):
	return map(int, f.readline().split())

def main():
	os.chdir("/Users/Jamie/Documents/Codejam")
	
	# f=open('input.txt','r')
	f=open('B-large.in','r')
	# f=open('A-large-practice.in','r')
	o=open('topscore.txt','w')
	
	T=int(f.readline())
	
	for j in range(T):
		L=readints(f)
		N=L.pop(0)
		S=L.pop(0)
		p=L.pop(0)
		tot=L
			
		result=0
		for t in tot:
			if 3*p<=t+2 and t>=p:
				result+=1
			elif 3*p<=t+4 and S>0 and t>=p:
				result+=1
				S-=1
		
		
		
		# print "Case #%s: %s\n" % (j+1,result)
		o.write("Case #%s: %s\n" % (j+1,result))
	f.close()
	o.close()

if __name__ == '__main__':
	main()


