N = int(raw_input())
w = "welcome to code jam"
for n in xrange(N):
	s = raw_input().strip()
	M = len(s)
	dp = [0]*M
	cnt = 0
	for i in xrange(M):
		if (s[i]==w[0]): cnt+=1
		dp[i] = cnt
	for i in xrange(1,len(w)):
		cnt = 0
		for j in xrange(M):
			if (s[j]==w[i]): cnt=(cnt+dp[j])%10000
			dp[j] = cnt
	print "Case #%d: %s" % (n+1, str(dp[M-1]).zfill(4))
	
