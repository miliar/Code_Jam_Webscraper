T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	M = N
	prevX = M%10
	M /= 10
	values = [prevX]
	count = 1
	while M!=0:
		X = M%10
		if X > values[-1]:
			values = [9]*count + [X-1]
		else: values.append(X)
		count += 1
		M/=10
	values = values[::-1]

	ans =0
	for j in range(len(values)):
		ans = ans*10 + values[j]	
	print "Case #%d: %d" % (i+1, ans)		
