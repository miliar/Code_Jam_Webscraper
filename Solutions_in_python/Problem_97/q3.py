count = input( )

from itertools import combinations

def numRecycled( a, b ):
	num = 0
	
	for n,m in combinations(range(a, b+1), 2):
		sn = str(n)
		sm = str(m)
		isRecycled = False
		if len(sn) == len(sm) and sn != sm:
			#print 
			#print sn, sm, '<<'
			for i in range(1, len(sn)):
				pushed = sn[i:] + sn[:i]
				#print sn, pushed
				if pushed == sm:
					isRecycled = True
					break
		if isRecycled:
			#print 'Y'
			num += 1
	
	return num

for i in range(count):
	(a, b) = raw_input().strip().split()
	a = int(a)
	b = int(b)
	
	print 'Case #%d:' % (i+1), numRecycled(a, b)