T = int(raw_input())
for case in xrange(T):
	A, B, K = map(int, raw_input().split())
	count = 0
	for x in xrange(A):
		for y in xrange(B):
			tmp = x & y
			if K > tmp:
				count += 1

	print "Case #" + str(case+1) + ":",count
