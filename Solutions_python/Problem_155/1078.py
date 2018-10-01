t = int(raw_input())

for i in xrange(t):
	arr = raw_input().split()
	n = int(arr[0])
	s = arr[1]
	ans = 0
	already_standing = 0
	for j in xrange(n+1):
		if int(arr[1][j]) > 0 and already_standing < j:
			ans += j-already_standing
			already_standing = j
		already_standing += int(arr[1][j])
		
	print "Case #"+str(int(i+1))+": "+str(ans)


