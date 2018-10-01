t = input()
for _ in xrange(t):
	n = input()
	m = map(int,raw_input().split())
	method_1 = 0
	method_2 = 0
	max_sub = 0
	for i in xrange(len(m)-1):
		before = m[i]
		after = m[i+1]
		if after - before < 0:
			method_1 += before - after
			if before - after > max_sub:
				max_sub = before - after
	for i in xrange(len(m)-1):
		before = m[i]
		after = m[i+1]
		if before > max_sub:
			method_2 += max_sub
		elif before > 0:
			method_2 += before
	print "Case #%d: %d %d" % (_+1,method_1,method_2)