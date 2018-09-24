#! /usr/bin/env python

def case(infile):
	S = int(infile.readline())
	readlist = lambda num: [l.strip() for l in [infile.readline() for i in xrange(num)]]
	engines = readlist(S)
	Q = int(infile.readline())
	queries = readlist(Q)
	out = 0
	while True:
		try:
			indices = [queries.index(engine) for engine in engines]
		except ValueError:
			return out
		maxindex = max(indices)
		out += 1
		queries = queries[maxindex:]
	return out
	
if __name__ == '__main__':
	infile = open('A-large.in')
	N = int(infile.readline())
	for casenum in xrange(N):
		output = case(infile)
		print 'Case #%d: %d' %(casenum+1, output)

