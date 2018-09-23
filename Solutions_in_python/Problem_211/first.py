from sys import stdin
t = int(stdin.readline())
for ca in xrange(1,t+1):
	n,k = map(int,stdin.readline().split())
	u = float(stdin.readline())
	a = map(float, stdin.readline().split())
	lo = 0.0
	hi = 1.0
	st = 500
	ans = 0 
	while st>=0:
		cur = 1
		mid = (lo + hi)/2.0
		x = 0
		for i in a:
			if i<mid:
				x+= mid - i; cur *= mid 
			else:
				cur *= i 
		#print "if we need",mid,x,cur             
		if x<= u:
			lo = mid
			ans = max(ans, cur)
		else:
			hi = mid
		st-=1            
	print "Case #%d: %.10f"%(ca,ans)