#python
from sys import stdin
f = open('test.out','w')

T = int(stdin.next())

for i in xrange(T):
	a,b,k = map(int,stdin.next().split())
	count = 0
	for j1 in xrange(a):
		for j2 in xrange(b):
			if j1&j2 < k:
				count += 1
	print count
	print>>f, 'Case #%d: %d' %(i+1,count)

