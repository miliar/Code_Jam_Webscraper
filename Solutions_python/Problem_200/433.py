t = int(input())
for c in range(1,t+1):
	n = list(input())
	n = [int(x) for x in n]
	minus = 0
	if len(n)==1:
		print("Case #{}: {}".format(c,n[0]))
	else:
		for i in range(len(n)-2,-1,-1):
			if n[i+1]<n[i]:
				for j in range(i+1,len(n)):
					n[j] = 9
				n[i] -= 1
		s = ""
		for j in n:
			s += str(j)
		s = int(s)
		print("Case #{}: {}".format(c,s))
		
		
