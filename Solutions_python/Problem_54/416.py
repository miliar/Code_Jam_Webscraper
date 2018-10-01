#! /usr/bin/python

def nwd(a,b):
	if a<0: a*=-1
	if b<0: b*=-1
	#print "nwd: ",a,b
	while(a>0 and b>0):
		#print "a:",a," b:",b
		if(a>b): a=a%b
		else: b=b%a
	if a>0:
		return a
	return b

def solve():
	tok=raw_input().split(" ")
	n=int(tok[0])
	num=int(tok[1])
	res=0
	for i in range(2,n+1):
		newval = int(tok[i])
		res=nwd(res,newval-num)
		#print res
	#print res
	return ((num+res-1)/res)*res-num

def main():
	z=int(raw_input())
	for i in range(0,z):
		print "Case #{0}: {1}".format(i+1,solve())
		z-=1

main()
