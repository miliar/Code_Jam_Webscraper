

def count_matches(a, b, n):
	a.sort()
	b.sort()
	res = 0
	i = 0
	j = 0
	while (i < n):
		while (j < n) and (b[j] < a[i]):
			j += 1
		if (j < n):
			res += 1
			j += 1
		i += 1
	return res	
	
inf = open("in.txt", 'r')
outf = open("out.txt", 'w')
t = int(inf.readline())
for k in xrange(0, t):
	n = int(inf.readline())
	naomi = map(float, inf.readline().split())
	ken = map(float, inf.readline().split())	
	outf.write("Case #" + str(k + 1) + ": ");
	outf.write(str(count_matches(ken, naomi, n)) + " ");
	outf.write(str(n - count_matches(naomi, ken, n)) + "\n")
outf.close()

