
substr = "welcome to code jam"
K = len(substr)

def Solve(s):
	N = len(s)
	t = [[0]*(N+1) for _ in range(K+1)]
	t[0] = [1] * (N+1)
	
	for i in range(1, K+1):
		for j in range(1, N+1):
			a, b = s[j-1], substr[i-1]
			t[i][j] = t[i][j-1]
			if a == b:
				t[i][j] += t[i-1][j-1]
			t[i][j] = t[i][j] % 10000
	# print '-' * 70
	# for row in t:
		# print row
		
	return t[K][N]
				

num_cases = int(raw_input())
for i in xrange(num_cases):
	res = Solve(raw_input().strip())
	print 'Case #%d: %04d' % (i+1, res % 10000)
