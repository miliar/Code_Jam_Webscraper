t = int(input())
for c in range(t):
	a,b = input().split()
	b = int(b)
	d = [0]*len(a)
	count = 0
	for i in range(len(a)):
		if a[i]=='+':
			d[i] = 1
	for i in range(0,len(a)-b+1):
		if d[i]==0:
			count += 1
			for j in range(i,i+b):
				d[j] = abs(d[j]-1)
	p = True
	if 0 in d:
		p = False
	if p:
		print("Case #{}: {}".format(c+1,count))
	else:
		print("Case #{}: IMPOSSIBLE".format(c+1))
