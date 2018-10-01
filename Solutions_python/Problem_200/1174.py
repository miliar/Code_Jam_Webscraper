for cas in range(1, input()+1):
	a=list(raw_input())
	for i in range(len(a)-1, 0, -1):
		if a == sorted(a):
			break
		a[i] = "9"
		if a[i-1] != "0":
			a[i-1] = str(int(a[i-1]) - 1)
	print "Case #%d: %d" % (cas, int("".join(map(str,a))))