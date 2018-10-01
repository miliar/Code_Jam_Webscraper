#! /usr/bin/python
from sys import stdin

def bitcount(N):
	ret=0
	while N!=0:
		if N&1:
			ret+=1
		N>>=1
	return ret
	
def compute(N,K):
	return bitcount(K%(1<<(N)))==N
	
if __name__=='__main__':
	data=stdin.readlines()
	T=int(data[0].strip())
	for case in xrange(1,T+1):
		(N,K)=map(int, data[case].split())
		answer=compute(N,K)
		if answer:
			print "Case #%d: %s"%(case,'ON')
		else:
			print "Case #%d: %s"%(case,'OFF') 
