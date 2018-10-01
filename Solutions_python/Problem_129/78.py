f = open('in')
t = int(f.readline())
for cas in xrange(1,t+1):
	n,m = map(int,f.readline().split(' '))
	eve = []
	more = 0
	for i in xrange(m):
		x,y,c = map(int,f.readline().split(' '))
		d = y-x-1
		more += c*(n+(n-d))*(d+1)/2
		eve.append([x,c,1])
		eve.append([y,c,-1])

	def comp(x,y):
		if x[0] != y[0]:
			if x[0] < y[0]:
				return -1
			elif x[0] > y[0]:
				return 1
			else:
				return 0
		else:
			if x[2] > y[2]:
				return -1
			elif x[2] < y[2]:
				return 1
			else:
				return 0
	eve.sort(cmp = comp)
	st = []
	ans = 0
	for x,c,lab in eve:
		if lab == 1:
			st.append([x,c])
		else:
			i = len(st)-1
			while (i >= 0) and (c > 0):
				if (c >= st[i][1]):
					d = x - st[i][0] - 1
					ans += st[i][1]*(n+n-d)*(d+1)/2
					c -= st[i][1]
					st.pop()
					i-=1
				else:
					d = x - st[i][0] - 1
					ans += c *(n+n-d)*(d+1)/2
					st[i][1] -= c
					c = 0
	ans = (more - ans) % 1000002013
	print "Case #%d: %d"%(cas,ans)


