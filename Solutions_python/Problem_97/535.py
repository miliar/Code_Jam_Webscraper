from math import log10

def problem():
	cases = int(raw_input())
	
	for i in xrange(cases):
		case(i + 1)

def case(i):
	n, m = [int(x) for x in raw_input().split(' ')]
	
	if m < 10:
		return result(i, 0)
	
	# number of digits
	d = int(log10(n)) + 1
	
	res = 0
	elist = range(1, d)
	
	for x in xrange(n, m + 1):
		reslist = set()
		
		for e in elist:
			# tail segment
			s = x % (10 ** e)
			# leading zero == bad ):
			if s < 10 ** (e - 1):
				continue
			# move tail to head
			r = x / (10 ** e) + s * (10 ** (d - e))
			# good?
			if r >= x or r < n or r > m:
				continue
			reslist.add(r)
		
		res += len(reslist)
	
	result(i, res)

def result(i, res):
	print 'Case #%d: %d' % (i, res)
	#pass

if __name__ == '__main__':
	problem()
