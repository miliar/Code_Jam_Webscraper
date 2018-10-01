t = int(input())
for tc in range(1,t+1):
	print("Case #{}: ".format(tc),end=' ')
	n,k = map(int,input().split())
	l = 0
	for i in range(k):
		a,b = map(int,input().split())
		a = n-a
		l = max(l,a/b)
	print(n/l)
