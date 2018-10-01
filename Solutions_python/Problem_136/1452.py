def shortest_time(c, f, x):
	rate = 2.0
	total_time = x / rate
	time = c / rate
	rate += f
	while total_time > time + x / rate:
		total_time = time + x / rate
		time += c / rate
		rate += f
		
	return total_time

for T in range(int(raw_input())):
	c, f, x = (float(n) for n in raw_input().split(' '))
	print "Case #%d: %0.7f" % (T+1, shortest_time(c, f, x))