
testcase = int(raw_input())
for caseno in xrange(1, testcase + 1):
	n = int(raw_input())
	l = map(float, raw_input().split())
	m = map(float, raw_input().split())
	l.sort()
	m.sort()
	j = 0
	count = 0
	for i in l:
		while j < n and m[j] < i:
			j += 1
		if j < n:
			count += 1
			j += 1
	z = n - count

	j = 0
	count = 0
	for i in l:
		if i < m[j]:
			continue
		count += 1
		j += 1
	y = count
	print "Case #%d: %d %d" % (caseno, y, z)
	