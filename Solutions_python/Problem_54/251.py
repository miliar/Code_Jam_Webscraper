#!/usr/bin/python
def gcd(a,b):
	while b>0: a,b = b,a%b
	return a

C = int(raw_input())
for cs in range(1,C+1):
	a = raw_input().split()
	N = int(a[0])
	for i in range(1,N+1):
		a[i] = int(a[i])
	g = 0;
	for i in range(1,N+1):
		for j in range(1,i):
			g = gcd(g,abs(a[i]-a[j]))
			if g == 1: break
		if g == 1: break
	
	res = (g-(a[1]%g))%g
	print 'Case #{0}: {1}'.format(cs,res) 
	
