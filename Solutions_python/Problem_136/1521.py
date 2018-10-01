t = input()
for case in range(1,t+1):
	c,f,k=[float(x) for x in raw_input().split()]
	ans = 0.0
	rate = 2.0
	while(True):
		way = [float('inf'),float('inf'),float('inf')]
		way[0] = k/rate
		way[1] = (c/rate)+(k/(rate+f))
		if(way[0]<way[1]):
			ans+=way[0]
			break
		ans += (c/rate)
		rate = rate+f
	print("Case #{}: {}".format(case, ans))
