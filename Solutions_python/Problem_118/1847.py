arr = [1, 4, 9]

def check(n):
	t = str(n * n)
	return int(t) if t == t[::-1] else 0

n = 1
while n < 1000000:
	s = str(n)
	p = s + s[::-1]
	r = check(int(p))
	if r: arr += [r]
	if len(s) % 2 == 1:
		p = s + s[-2::-1]
		r = check(int(p))
	n += 1

TC = input()
for T in xrange(TC):
	a, b = map(int, raw_input().split())
	print 'Case #%d: %d' % (T+1, len(filter(lambda x: a <= x <= b, arr)))