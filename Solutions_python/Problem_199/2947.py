t = int(input())
for i in range(t):
	a,b = raw_input().split()
	a=str(a)
	b=int(b)
	count=0
	while "-" in a:
		n = a.index("-")
		a = list(a)
		if n+b <= len(a):
			for m in range(n,n+b):
				if a[m] == "+":
					a[m] = "-"
				else:
					a[m] = "+"
			count+=1
		else:
			print "Case " + "#" + str(i+1) + ": " + "IMPOSSIBLE"
			break
	if "-" not in a:
		print "Case " + "#" + str(i+1) + ": " + str(count)
