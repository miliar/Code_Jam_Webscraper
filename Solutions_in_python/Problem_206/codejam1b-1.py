t=int(input())
for k in range(t):
	d,n=[int(i) for i in input().strip().split()]
	mm = 0
	for _ in range(n):
		a,b=[int(i) for i in input().strip().split()]
		if((d-a)/b > mm):
			mm = (d-a)/b
	print("Case #"+str(k+1)+":",d/mm)