for i in range(int(input())):
	n,k = map(int,input().split())
	ma = n//2
	mi = n//2 - abs(n%2-1)
	lst = sorted([ma,mi])
	for j in range(k-1):
		t = lst[-1]
		del lst[-1]
		ma = t//2
		mi = t//2 - abs(t%2-1)
		lst.append(ma)
		lst.append(mi)
		lst.sort()
	print("Case #"+str(i+1)+":",ma,(mi+abs(mi))//2)