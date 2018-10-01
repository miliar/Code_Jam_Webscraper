T = int(raw_input())

for t in xrange(T):
	A, B, K = map(int, raw_input().split())
	count = 0
	for a in xrange(A):
		for b in xrange(B):
			num = a & b
			if num < K: count += 1
	
	print("Case #{0}: {1}".format((t + 1), count))
