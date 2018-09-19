def can_p(t, p):
	return t - p - max(0, (p - 1)) * 2 >= 0

def can_ps(t, p):
	return t - p - max(0, (p - 2)) * 2 >= 0

T = int(raw_input())
for i in xrange(T):
	l = map(int, raw_input().split())
	N = l.pop(0)
	S = l.pop(0)
	p = l.pop(0)
	r = 0
	for t in l:
		if can_p(t, p):
			r += 1
			continue
		if can_ps(t, p) and S > 0:
			r += 1
			S -= 1
			continue
	assert len(l) == N
	print 'Case #%i:' % (i + 1), r
