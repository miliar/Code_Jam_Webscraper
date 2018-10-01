for t in range(int(input())):
	n = int(input())
	x = list(map(float,input().split(" ")))
	y = list(map(float,input().split(" ")))
	x.sort()
	y.sort()
	win=n
	i=0
	j=0
	while(j<n):
		if(x[i]<y[j]):
			i+=1
			j+=1
			win-=1
		else:
			j+=1

	i=n-1;j=n-1;fwin=0
	while(j>=0):
		if(x[i]>y[j]):
			i-=1
			j-=1
			fwin+=1
		else:
			j-=1
	print("Case #{}: {} {}".format(t+1,fwin,win))
