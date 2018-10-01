#! /usr/bin/python
f=open('C-small-attempt0.in','r')

def count(s,n):
	welcome='welcome to code jam'
	if n>=len(welcome): return 1

	index=s.find(welcome[n],0)
	indices=[]
	while index>-1:	
		indices.append(index)
		index=s.find(welcome[n],index+1)

	sum=0
	for index in indices:
		sum+=count(s[index+1:],n+1)
	return sum

N=int(f.readline())
for n in range(N):
	case=f.readline()
	print 'Case #{0}: {1:04}'.format(n+1,count(case,0)%1000)

