def solve(n, k):
	if n == k: return (0,0)
	if k == 1:
		n1 = n//2
		n2 = n-1-n1
		x = [n1, n2]
		x.sort()
		return (x[1],x[0])
	s = []
	s += [0,n+1]
	s.append((n+1)//2)
	s.sort()
	_k = k-1
	l = []
	max = [-1,-1]
	while _k > 1:
		l = []
		for i in range(len(s)-1):
			l.append([i,s[i+1]-s[i]])
		max = [-1,-1]
		for i in range(len(l)):
			if max[1] < l[i][1]:
				max = l[i]
		s.insert(max[0]+1,s[max[0]] + (max[1]+1)//2)
		_k -= 1
	l = []
	for i in range(len(s)-1):
		l.append([i,s[i+1]-s[i]])
	max = [-1,-1]
	for i in range(len(l)):
		if max[1] < l[i][1]:
			max = l[i]
	num = max[1] -1
	
	n1 = (num)//2
	n2 = num-1-n1

	x = [n1, n2]
	x.sort()
	return (x[1],x[0])


T = int(input())

N, K = [], []

for i in range(T):
	x = input().split()
	N.append(int(x[0]))
	K.append(int(x[1])) 

for cnt in range(T):
	Ms, ms = solve(N[cnt], K[cnt])

	print('Case #%d: '%(cnt+1),end='')
	print('%d %d'%(Ms, ms))