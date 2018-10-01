t = int(raw_input())
for ti in xrange(t):
	temp = raw_input().split()
	k = int(temp[1])
	arr = []
	for i in temp[0]:
		if (i=='+'):
			arr.append(1)
		else:
			arr.append(0)

	ptr = 0
	count = 0
	while(ptr<=len(arr)-k):
		if (arr[ptr]==0):
			count += 1
			for j in xrange(ptr,ptr+k):
				arr[j] = 1-arr[j]
		ptr += 1
	flag = 1
	for i in arr:
		if (i==0):
			flag = 0
			print "Case #"+str(ti+1)+": IMPOSSIBLE"
			break

	if (flag==1):
		print "Case #"+str(ti+1)+": "+str(count)