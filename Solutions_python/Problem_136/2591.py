t = input()
for i in range(t):
	r = 2.0
	line = raw_input()
	values = line.split()
	row = [float(value) for value in values]
	c = row[0]
	f = row[1]
	x = row[2]
	done = 0
	time = 0.0
	while(done == 0):
		t = time + x/r
		r2 = r + f
		t2 = time + c/r +  x/r2
		if(t2 < t):
			time += c/r
			r = r2
		else:
			time = t
			done = 1
	
	print "Case #{0}: {1:.7f}".format(i+1,time)
		
	