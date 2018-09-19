t = input()
for case in range(1,t+1):
	n = input()
	c = sorted([float(x) for x in raw_input().split()])
	p = sorted([float(x) for x in raw_input().split()])
	i,j=0,0
	ans = [0,n]
	while(i<n and j<n):
		if(c[i]>p[j]):
			ans[0] += 1
			i += 1
			j += 1
		else:
			i += 1
	i,j=0,0
	while(i<n and j<n):
		if(c[i]<p[j]):
			ans[1] -= 1
			i += 1
			j += 1
		else:
			j += 1
	print("Case #{}: {} {}".format(case, ans[0],ans[1]))
