# Inputs
T = 0
ip = open("B-large.in", 'r')
op = open("output.txt", 'w')
T = int(ip.readline().rstrip())

for i in range(T):
	s = ip.readline().rstrip().split(' ')
	c = float(s[0])
	f = float(s[1])
	x = float(s[2])
	# c, f, x
	y = 0
	pastTime = 0
	t1 = 0
	t2 = 0
	r = 2
	n = 0

	while True:
		#global pastTime
		t1 = x / r 	# Wait time
		# "t1 = " ,t1
		t2 = (c/r) + (x/(r+f))	# Buy time
		# "t2 = ", t2
		if t1 <= t2:
			y = t1 + pastTime
			# "y = ", y
			break
		else:
			pastTime += c/r
			# "pastTime = ", pastTime
			n += 1
			# "n = ", n
			r = 2 + n*f
			# "r = ", r

	op.write("Case #"+str(i+1)+": " + str(y) + '\n')

ip.close()
op.close()