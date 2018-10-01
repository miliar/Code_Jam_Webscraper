#!/bin/python

def allset(s):
	l=len(s)
	ans=-1
	for i in range(0,l-1):
		if s[i]>s[i+1]:
			ans=i
			break
	return ans

def change(inp):
	index = allset(inp)
	ans=""
	if index==-1:
		ans=inp
	else:
		nines="9"*(len(inp)-index-1)
		ans=inp[:index]
		ans=ans+str(int(inp[index])-1)
		ans=ans+nines
	if ans[0]=="0":
		ans=ans[1:]
	return ans


tcases=int(raw_input())
j=1
while tcases>0:
	inp = raw_input()
	while True:
		inp=change(inp)
		if allset(inp)==-1:
			break
	print "Case #"+str(j)+": "+inp
	j=j+1
	tcases-=1