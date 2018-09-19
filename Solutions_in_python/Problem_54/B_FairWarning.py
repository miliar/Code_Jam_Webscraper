input = open('B-large.in', 'r')
output = open('B-large.out', 'w')
def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)

for i, line in enumerate(input):
	try:
		n = map(int, line.split(' ')[0])
		g = map(long, line.split(' ')[1:])
	except:
		continue
	m = min(g)
	d = 0
	for v in g:
		if v != m:
			d = gcd(v - m, d)
	m %= d
	
	if m > 0:
		m = d - m
	print >>output,"Case #%d: %d" % (i, m)

output.close()
