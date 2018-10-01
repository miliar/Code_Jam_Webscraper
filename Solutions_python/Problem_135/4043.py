
def read_input():
	ans = int(raw_input())
	arr = []
	for j in range(4):
		arr.append([int(k) for k in raw_input().split(' ')])
	return ans, arr
		

t = int(raw_input())
for i in range(t):
	ans1, arr1 = read_input()
	ans2, arr2 = read_input()	
	
	f1 = arr1[ans1-1]
	f2 = arr2[ans2-1]
	
	c,ans = 0,0
	for j in f1:
		if j in f2:
			c += 1
			ans = j
		if c > 1:
			print 'Case #{0}: Bad magician!'.format(i+1)
			break
	if c == 0:
		print 'Case #{0}: Volunteer cheated!'.format(i+1)
	elif c == 1:
		print 'Case #{0}: {1}'.format(i+1,ans)
	
	
	
