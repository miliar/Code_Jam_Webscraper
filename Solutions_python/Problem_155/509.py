def solution():
	s, x = raw_input().split()
	s = int(s)
	cur = 0
	ans = 0
	for j in xrange(s + 1):
		q = int(x[j])
		if (j > cur):
			ans += j - cur
			cur = j
		cur += q
	return ans 

t = int(raw_input())

for tt in xrange(t):
	print "Case #{}: {}".format(tt + 1, solution())