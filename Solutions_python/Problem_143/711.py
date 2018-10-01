t = input()
for t in range(0,t):
	a,b,k = map(int, raw_input().split())
	cnt = 0
	for i in range(0,a):
		for j in range(0,b):
			if i & j < k :
				cnt = cnt + 1
	print "Case #%d: %d" % (t+1,cnt)