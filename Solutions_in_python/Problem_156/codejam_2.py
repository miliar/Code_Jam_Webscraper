test = int(raw_input())
for x in range(test):
	it = int(raw_input())
	dt = {}
	inp = str(raw_input()).split()
	for i in range(len(inp)):
		dt[int(inp[i])] = dt.get(int(inp[i]), 0) +1
	lst = dt.keys()
	maximum = max(lst)
	ans = maximum
	for i in range(1,1001):
		temp = 0
		for j in lst:
			if temp < maximum:
				if(j%i==0):
					temp += (j/i - 1)*dt[j]
				else:
					temp += (j/i)*dt[j]
		temp += i
				
		if temp < ans:
					ans = temp
	print "Case #" + str(x+1) +": " + str(ans)