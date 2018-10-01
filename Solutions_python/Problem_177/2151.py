def count_sheep(N):
	seen = []
	if int(N) == 0:
		return None
	i = 0
	while True:
		n = (i + 1) * int(N)
		n_str = str(n)
		for digit in n_str:
			if digit not in seen:
				seen.append(digit)
		if len(seen) == 10:
			return n
		i += 1

#Get input
t = int(raw_input().strip())
tests = []
for _ in xrange(t):
	tests.append(raw_input().strip())
	
#do stuff
for i in xrange(t):
	sheep = count_sheep(tests[i])
	if sheep is None:
		sheep = "INSOMNIA"
	print "Case #{0}: {1}".format(i+1, sheep)
