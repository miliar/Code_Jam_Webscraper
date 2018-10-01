import sys

def parse(s):
	p = []
	c = s[0]
	i = 1
	for x in s[1:]:
		if x == c:
			i += 1
		else:
			p.append( (c, i) )
			c = x
			i = 1
	p.append( (c, i) )
	return p

def find_min(counts):
	if len(counts) == 2:
		return abs(counts[0] - counts[1])
	else:
		m = 1e10
		for x in xrange(min(counts), max(counts) + 1):
			s = 0
			for c in counts:
				s += abs(x - c)
			if s < m:
				m = s
		return m

def solve(strings):
	p = [parse(s) for s in strings]
	
	lengths = [len(a) for a in p]
	if min(lengths) != max(lengths):
		return 'Fegla Won'

	n = lengths[0]
	score = 0
	
	for i in xrange(n):
		chars = [a[i][0] for a in p]
		if min(chars) != max(chars):
			return 'Fegla Won'

		counts = [a[i][1] for a in p]
		score += find_min(counts)

	return score

T = int(sys.stdin.readline())
for t in range(1, T + 1):
	n = int(sys.stdin.readline())
	s = [sys.stdin.readline().strip() for i in xrange(n)]
	print "Case #" + str(t) + ":", solve(s)