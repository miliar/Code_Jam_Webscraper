test=int(input())
for tt in range(test):
	c,f,x = (float(i) for i in input().split(' '))
	r=2
	ans=0
	while True:
		if x/r > c/r+x/(f+r):
			ans+=c/r
			r+=f
		else:
			ans+=x/r
			break
	print('Case #%d: %f' % (tt+1,ans))
