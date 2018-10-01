t = int(input())
for t_index in range(t):
	d,n = input().split()
	d = int(d)
	n = int(n)
	tmax = 0
	for i in range(n):
		k,s = input().split()
		k = int(k)
		s = int(s)
		t = (d-k)/s
		if t > tmax:
			tmax = t
	v = d/tmax
	print("Case #"+str(t_index+1)+": "+str(v))
