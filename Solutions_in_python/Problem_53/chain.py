inf = open("a.in", "r")
ouf = open("a.out", "w")
T = int(inf.readline())
for t in range(T):
	[n, k] = [int(i) for i in inf.readline().split()]
	mask = (1 << n) - 1
	print >> ouf, "Case #" + str(t + 1) + ":",
	if (mask & k) == mask: 
		print >> ouf, "ON"
	else:
		print >> ouf, "OFF"
inf.close()
ouf.close()