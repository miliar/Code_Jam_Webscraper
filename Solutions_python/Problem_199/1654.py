# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:59:29 2017

@author: adobe
"""
magic = lambda nums: int(''.join(str(i) for i in nums))
from math import *
N=input()
ans=[]

def flip(seq):
	for j,con in enumerate(seq):
		if con=='-':
			seq[j]='+'
		else:
			seq[j]='-'
	return seq


for i in range(N):
	sen=raw_input()
	(seq,k)=sen.split()
	k=int(k)
	seq=list(seq)
	count=0
	for j,_ in enumerate(seq[:1-k]):
		if seq[j]=='-':
			seq[j:j+k]=flip(seq[j:j+k])
			# print seq
			count+=1
	for check in seq[-k:]:
		if check == '-':
			count=-1
	if count == -1:
		ans.append("IMPOSSIBLE")
	else:
		ans.append(str(count))
# print ans
for j,con in enumerate(ans):
	print "Case #"+str(j+1)+": "+str(con)