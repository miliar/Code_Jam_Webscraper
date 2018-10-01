#!/usr/bin/python

tc	= int(raw_input())

for i in xrange(1,tc+1):
	cash	= 0;

	lst 	= map(int, raw_input().split())
	k	= lst[1]
	n	= lst[2]
	q 	= map(int, raw_input().split())
	
	for j in xrange(0,lst[0]):
		ride	= []
		while (len(q) > 0):
			s	= sum(ride)
			if(s + q[0] <= k):
				ride.append(q.pop(0))
			else:
				break
		cash	+= sum(ride);
		q	+= ride;
	
	print ''.join(['Case #',str(i),': ',str(cash)])

