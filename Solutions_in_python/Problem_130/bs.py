from itertools import permutations
T = int(raw_input())

def hah(x,n):
	if x==0:
		return 0
	good = x
	for i in range(n):
		if good==2**(n-i)-1:
			return good
		good = good - good/2
	print x,n,good
	return good


def qiu(x,n):
	good = hah(x,n)
	bad = 2**n-1-hah(2**n-1-x,n)
	return good,bad


for cas in range(1,T+1):
	n,p = map(int,raw_input().split())
	guar = 0 
	poss = 0

	l=0
	r=2**n
	while l+1<r:
		m=(l+r)/2
		good,bad=qiu(m,n)
		if good<p:
			l=m
		else:
			r=m
	poss=l

	l=0
	r=2**n
	while l+1<r:
		m=(l+r)/2
		good,bad=qiu(m,n)
		if bad<p:
			l=m
		else:
			r=m
	guar = l
	print "Case #%d:" % cas,guar,poss

