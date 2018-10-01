def solve(a,b):
	count=0
	#pre-calced in small input case
	fairpalin=[1,4,9,121,484]
	for n in fairpalin:
		if a<=n and n<=b:
			count+=1
	return count

for n in range(0,input()):
	a,b=map(int,raw_input().split())
	print("Case #{0}: {1}".format(n+1,solve(a,b)))
