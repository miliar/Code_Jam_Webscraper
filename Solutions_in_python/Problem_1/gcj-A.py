import sys

n = int(sys.stdin.readline())

for i in xrange(1,n+1):
	s = int(sys.stdin.readline())
	engines = []
	for x in xrange(s):
		engines.append(sys.stdin.readline())
	
	q = int(sys.stdin.readline())
	if q == 0:
		print "Case #%u: %u" % (i, 0)
		continue
	queries = []
	for x in xrange(q):
		queries.append(sys.stdin.readline())
	
	switches = 0
	last = 0
	while last < q:
		lengths = []
		for e in engines:
			curr = last
			while curr < q:
				if queries[curr] == e:
					break
				curr += 1
			lengths.append(curr)
		last = max(lengths)
		switches += 1
		
	print "Case #%u: %u" % (i, switches-1)