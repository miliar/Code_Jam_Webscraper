t=int(raw_input())
for case in range(t):
	n=int(raw_input())
	arr=[int(x) for x in raw_input().split()]
	cnt=0
	for i in range(1,n):
		if arr[i]<arr[i-1]:  
			cnt+=arr[i-1]-arr[i]
	# print cnt
	# diff=arr[-2]-arr[-1]
	# print "Adwad",arr[-2],arr[-1],diff
	diff=0
	for i in range(n-1):
		diff=max(arr[i]-arr[i+1], diff)

	
	cnt2=0
	if diff>=0:
		for i in range(n-1):
			if arr[i]<diff:  
				cnt2+=arr[i]
			else:
				cnt2+=diff
	print "Case #{}: {} {}".format(case+1,cnt,cnt2)