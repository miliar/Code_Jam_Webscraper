#!/usr/bin/python

gcd=lambda a,b:a if not b else gcd(b,a%b)

#read=open('input.txt').readline
#out=open('output.txt','w').write
#read=open('B-small-attempt0.in').readline
#out=open('B-small-attempt0.out','w').write
read=open('B-large.in').readline
out=open('B-large.out','w').write

t=int(read())
for test in range(t):
	inp=map(int,read().split())
	n=inp[0]
	l=inp[1:]
	r=[abs(l[i]-l[j]) for i in range(n-1) for j in range(i+1,n)]
	d=reduce(gcd,r)
	low = min(l)
	ans=d-(low-1)%d-1
	print d,low
	out("Case #%d: %d\n"%(test+1,ans))
	#print test