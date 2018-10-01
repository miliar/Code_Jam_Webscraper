tests = int(raw_input(''))
for t in xrange(tests):
	r = raw_input('').split()
	C = float(r[0])
	F = float(r[1])
	X = float(r[2])

	time = 0.0
	increase = 2.0
	result = 100000000000000.0

	bound = int( (F*X - 2.0*C)/(F*C) )
	for i in xrange(bound+10):
		result = min(result, time + X/increase)
		time += C/increase
		increase += F
	print "Case #"+str(t+1)+":", result