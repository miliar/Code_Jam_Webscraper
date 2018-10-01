import sys



t = int(sys.stdin.readline())

for case in range(1, t+1):
	
	A,B,K = map(int, sys.stdin.readline().split())
	count = 0

	for i in range(A):
		for j in range(B):
			if (i & j) < K: count += 1

	print "Case #{0}: {1}".format(case, count)
