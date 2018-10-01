#!/usr/bin/env python

import sys

def solvecase(A,B):
	count=0
	for i in range(A,B):
		idigitlist=[int(x) for x in list(str(i))]
		s=[]
		for j in range(1,len(idigitlist)):
			m=int(''.join([str(x) for x in idigitlist[-j:]+idigitlist[:-j]]))
			if i<m and m<=B and (m not in s):
				count+=1
				s.append(m)
	return count


if __name__=="__main__":
	inpfile=open(sys.argv[1],'r')
	T=int(inpfile.readline())
	for i in range(0,T):
		inpline=inpfile.readline().split()
		count=solvecase(int(inpline[0]),int(inpline[1]))
		print('Case #'+str(i+1)+':',count)
	inpfile.close()




