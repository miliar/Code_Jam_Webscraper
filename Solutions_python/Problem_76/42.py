#!/usr/bin/python

T=input()
I=0

while T>0:
	T-=1
	I+=1
	n=input()
	candy = map(long,raw_input().split())
	candy.sort()
	sum = 0
	s=0
	for i in candy:
		sum^=i
		s+=i
	if sum!=0:
		print 'Case #%d: NO' % I
	else:
		print 'Case #%d: %d' % (I,s-candy[0])

