#intog

def find_min(s,n):
	total = 0
	N = len(s)
	flip_arr = [False]*N
	flipped_arr = [False]
	flipped = False 
	for i in xrange(N):
		flip_arr[i] = (s[i]=='-' and not flipped) or (s[i]=='+' and flipped)
		flipped = (flip_arr[i] != flipped) 
		flipped = ((False if i < n-1 else flip_arr[i-n+1]) != flipped)
		flipped_arr.append(flipped)
		total+= (1 if flip_arr[i] else 0)
		if flip_arr[i] and (i+n > N): 
			#print 'flip_arr', flip_arr
			#print 'filpped_arr', flipped_arr
			return -1 	
	return total
T = int(raw_input())
for t in xrange(T):
	s, n = raw_input().split(' ')
	n = int(n)
	m = find_min(s, n)
	print 'Case #{0}: {1}'.format(t+1, 'IMPOSSIBLE' if m==-1 else m)
