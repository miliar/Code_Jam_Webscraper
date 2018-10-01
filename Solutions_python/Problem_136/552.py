with open("input.txt", 'r') as infile:
	cases = int(infile.readline())
	results = [0] * cases
	
	for case in range(cases):

		
		param = infile.readline().split()
		C = float(param[0])
		F = float(param[1])
		X = float(param[2])
		cps = 2.0
		tot_time = C / cps  # start off at the purchase of first farm
		if X < C:
			results[case] = X / cps
			continue
		# assuming only 1 optimum
		while 1 == 1:
			cur_time = (X - C) / cps  # how long until X without farm
			new_time = (X) / (cps + F)  # how long it would take buying the farm
			
			"""
			print("case: ", case)
			print("Total time up to now: ", tot_time)
			print("Without farm: {} With farm: {}".format(cur_time, new_time))
			print("cps: ", cps)
			"""
			
			if (new_time < cur_time):
				# buy new farm
				# cookies -= C
				cps += F
				tot_time += C / cps  # advance to next decision of whether to buy farm
			else:
				# don't buy farm, just wait until X
				tot_time += cur_time
				results[case] = tot_time
				break  # completed case
			
	# print out case results
	for case in range(cases):
		print("Case #{}: {:.7f}".format(case + 1, results[case]))