t = int(input())
for _ in range(t):
	n = int(input())
	l = [0]
	for a in range(n,0,-1):
		l1 = list(str(a))
		if len(l1) == 1:
			l[0] = a
			break
		else:
			flag = 0
			for b in range(len(l1)-1):
				if int(l1[b]) <= int(l1[b+1]):
					flag = 1
				else:
					flag =0
					break
			if flag == 1:
				l[0] = a
				break
	print("Case #"+str(_+1)+": "+str(l[0]))

