def P2(N):
	l = list(map(int,list(str(N))))
	for i in range(len(l)-1):
		if l[i] <= l[i+1]:
			continue
		l[i] -= 1
		for j in range(i+1,len(l)):
			l[j] = 9
		return P2(int(''.join(list(map(str,l)))))
		
	return int(''.join(list(map(str,l))))



T = int(input())
for t in range(T):
	print("Case #%d: %d"%(t+1,P2(int(input()))))
