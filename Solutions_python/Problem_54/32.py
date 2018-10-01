def gcd(x,y):
	while x:
		x, y = y % x, x
	return y

t = input()

for ii in range(0, t):
	s = raw_input()
	nx = s.split(' ')
	n = int(nx[0])
	x = map(long, nx[1:n + 1])

	g = max(x[0], x[1]) - min(x[0], x[1])
	for i in range(0, n):
		for j in range(i, n):
			g = gcd(g, max(x[i], x[j]) - min(x[i], x[j]))

	minimal = min(x)
	if minimal % g == 0:
		result = 0
	else:
		result = g - minimal % g
	
	print "Case #{0}: {1}".format(ii + 1, result)

