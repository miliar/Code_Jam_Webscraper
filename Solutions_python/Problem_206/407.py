for _ in xrange(input()):
	D, N = map(int, raw_input().split())

	t = 0
	for i in xrange(N):
		K, S = map(float, raw_input().split())
		t = max(t, (D - K) / S)



	print "Case #%d:" % (_ + 1), D / t
