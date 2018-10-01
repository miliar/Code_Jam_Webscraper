def do():
	n,m=map(int,raw_input().split())
	a=[]
	for i in range(n):
		a.append(map(int,raw_input().split()))
	for i in range(n):
		for j in range(m):
			b1=True
			b2=True
			for k in range(n):
				if a[k][j]>a[i][j]:
					b1=False
			for k in range(m):
				if a[i][k]>a[i][j]:
					b2=False
			if not b1 and not b2:
				return False
	return True
for i in range(input()):
	print "Case #%d:"%(i+1),
	if do():
		print "YES"
	else:
	 	print "NO"
