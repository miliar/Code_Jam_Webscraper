t=input()
for i in range(1,t+1):
	n=input()
	a=map(float,raw_input().split())
	b=map(float,raw_input().split())
	a.sort()
	b.sort()
	e=a[::-1]
	f=[]+b
	d=0
	g=n-1
	for j in range(n):
		if(f[g]>e[j]):
			f.pop(g)
		else:
			f.pop(0)
			d=d+1
		g=g-1
	c=-1
	for j in range(0,n+1):
		e=a[j:n+1]
		f=b[0:n+1-j]
		for k in range(0,n-j):
			if(f[k]>e[k]):
				break
			if(k+1==n-j):
				c=n-j
		if(c!=-1):
			break
	if(c==-1):
		c=0
	print "Case #"+`i`+":",c,d
