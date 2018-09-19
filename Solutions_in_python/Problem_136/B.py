test_num = int(raw_input().strip())
for i in xrange(test_num):
	t_gain = 2.0
	(C, F, X) = [float(elem) for elem in raw_input().strip().split()]
	x_time = round(X/t_gain,7)
	
	total_time_without_f = x_time
	total_time_with_f = x_time
	total_time = 0


	while (total_time_with_f <= total_time_without_f):
		total_time_without_f = total_time_with_f
		f_time = round(C/t_gain, 7)	
		t_gain = t_gain + F
		x_time = round(X/t_gain,7)
		total_time = total_time + f_time 
		total_time_with_f = total_time + x_time
		#print total_time_without_f, total_time_with_f
		#iterations = iterations - 1
		#if iterations == 0:
		#	break
	print "Case #%d: %0.07f" % ((i+1),total_time_without_f)	