a=raw_input()
t=int(a)
thecase=1
for i in range(0,t):
	a=raw_input()
	n=int(a)
	mymap={}
	for j in range(0,n):
		a=raw_input()
		mymap[a]=j
	flag=[0]*n
	cnt=0
	ans=0
	a=raw_input()
	q=int(a)
	for j in range(0,q):
		a=raw_input()
		now=mymap[a]
		if(flag[now]==0):
			flag[now]=1
			cnt=cnt+1
		if(cnt==n):
			flag=[0]*n
			ans=ans+1
			cnt=1
			flag[now]=1
	print "Case #"+str(thecase)+": "+str(ans)
	thecase=thecase+1

