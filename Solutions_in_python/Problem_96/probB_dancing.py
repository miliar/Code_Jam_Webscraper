import sys

def solve_case( surprise, p, googlers ):
	if p <= 0:
		base_limit = 0
		surprise_limit = 0
	elif p <= 1:
		base_limit = 1
		surprise_limit = 1
	else:
		base_limit = p + 2 * ( p - 1 )
		surprise_limit = p + 2 * ( p - 2 )

	result = 0
	surprise_left = surprise
	for g in googlers:
		if g >= base_limit:
			result += 1
		elif g >= surprise_limit and surprise_left > 0:
			result += 1
			surprise_left -= 1
	return result

t = int(sys.stdin.readline())

for i in xrange(t):
	data = sys.stdin.readline().split()
	n = int(data[0])
	s = int(data[1])
	p = int(data[2])
	g = map( int, data[3:] )
	print 'Case #%d: %d' % ( i + 1, solve_case( s, p, g ) )