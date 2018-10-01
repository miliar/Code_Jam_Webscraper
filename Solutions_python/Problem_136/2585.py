for i in range(input()):
	c, f, x = [float(a) for a in raw_input().split()]
	res = x / 2.0
	current_time = 0.0
	current_rate = 2.0
	while current_time < res:
		current_time += c / current_rate
		current_rate += f
		total_time = current_time + x / current_rate
		if res > total_time:
			res = total_time


	print 'Case #%d: %.7f' %(i+1, res)
