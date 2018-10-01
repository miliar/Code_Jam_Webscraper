# -*- coding: iso-8859-2 -*-


def gcd(a,b):
	if b==0: return a
	return gcd(b,a%b)



T = input()
for test in range (1,T+1):
	L = raw_input().split(" ")
	n = int(L[0])
	P = []
	for i in range(1,n+1):
		P.append(int(L[i]))
	P.sort()
	d = P[n-1]-P[n-2]
	for i in range(2,n):
		d = gcd(d,P[n-i]-P[n-i-1])
	ret = (d - P[0]%d)%d
	print "Case #"+str(test)+": "+str(ret) 

