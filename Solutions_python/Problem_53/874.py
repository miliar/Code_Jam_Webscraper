f = open('A-large.in', 'r')
f2 = open('out.txt', 'w')

for indx, line in enumerate(f):
	if indx == 0:
		T = int(line)
	else:
		s = line.split()
		N = long(s[0])
		K = long(s[1])
		if (K+1)%(2**N) == 0:
			print >> f2, "Case #" + str(indx) + ": ON"
		else:
			print >> f2, "Case #" + str(indx) + ": OFF"
f.close()
f2.close()