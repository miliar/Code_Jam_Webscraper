t = int(input())
for tc in range(1,t+1):
	r,c = map(int,input().split())
	l = []
	for i in range(r):
		l.append(list(input()))
	val = ''
	ans = ''
	for i in range(r):
		j = 0
		while j<c:
			if l[i][j]!='?':
				val = l[i][j]
				j += 1
				while j<c and l[i][j]=='?' :
					l[i][j] = val
					j+=1
			else:
				j += 1
	for i in range(r):
		j = c-1
		while j>=0:
			if l[i][j]!='?':
				val = l[i][j]
				j -= 1
				while j>=0 and l[i][j]=='?':
					l[i][j] = val
					j-=1
			else:
				j -= 1
	for i in range(c):
		j = 0
		while j<r:
			if l[j][i]!='?':
				val = l[j][i]
				j += 1
				while j<r and l[j][i]=='?':
					l[j][i] = val
					j += 1
			else:
				j += 1
	for i in range(c):
		j = r-1
		while j>=0:
			if l[j][i]!='?':
				val = l[j][i]
				j -= 1
				while j>=0 and l[j][i]=='?':
					l[j][i] = val
					j -= 1
			else:
				j -= 1

				
				
	print("Case #{}:".format(tc))
	for i in range(r):
		print(''.join(l[i]))
