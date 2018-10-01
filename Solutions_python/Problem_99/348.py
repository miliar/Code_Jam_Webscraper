inp = file("input.in")
n = eval(inp.readline())
out = file("output.txt", "w")

for t in xrange(n):
	A, B = inp.readline().split()
	A = eval(A)
	B = eval(B)
	C = B - A # rest
	p = inp.readline().split()
	prob = 1
	for i in xrange(A):
		p[i] = eval(p[i])
		prob = prob * p[i]
	exp = 1 + B + 1 # enter and retype
	for	i in xrange(A):
		aux = i + C + i + 1 + (B + 1)*(1 - prob)
		if aux < exp:
			exp = aux
		prob = prob / p[A - i - 1]
	
	out.write("Case #%d: %f" %(t + 1, exp) + "\n")
