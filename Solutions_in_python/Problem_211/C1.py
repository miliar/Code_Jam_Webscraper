T = int(input())
for loop in range(1,T+1):
	N,K = [int(x) for x in input().split()]
	U = float(input())
	l = [float(x) for x in input().split()]
	l = sorted(l)
	n = len(l)
	while U>0.0:
		end = False
		entered = False
		for x in range(n-1):
			entered = True
			d = l[x+1] - l[x]
			if x==(n-2) and d==0:
				end = True
			dd = d * (x+1)
			if dd <= U:
				U = U - dd
				for i in range(x+1):
					l[i] = l[i] + d
			else:
				d = U / (x+1)
				U = 0
				for i in range(x+1):
					l[i] = l[i] + d
		if end or not entered:
			d = U/n
			U = 0
			for i in range(n):
				l[i] = l[i] + d
	ans = 1
	for i in range(n):
		ans = ans*l[i]
	print("Case #",loop,": ",ans,sep="")
