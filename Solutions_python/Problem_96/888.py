num_testcase = int(raw_input())
for i in range(0,num_testcase):
	line = raw_input()

	params = line.split(' ')
	s = int(params[1])
	p = int(params[2])

	nums = [int(n) for n in params[3:]]
	new_nums = [(int(num/3), num%3) for num in nums]

	new_nums.sort()
	new_nums.reverse()

	counts = 0
	# print line
	# print new_nums
	for (base,mod) in new_nums:
		if mod == 0 and base >= p:
			counts += 1
		elif mod == 2 and (base + 1) >= p:
			counts += 1
		elif mod == 1 and (base + 1) >= p:
			counts += 1
		elif s != 0:
			if mod == 2 and base + 2 >= p:
				counts += 1
				s -= 1
			elif mod == 0 and base + 1 >= p and base != 0:
				counts += 1
				s -= 1


		"""
		if base != 9:
			if base >= p or (mod == 1 and (base + mod) >= p):
				counts += 1
			else:
				if s != 0:
					if mod == 2 and (base+2)>= p:
						counts += 1
						s -= 1
					elif mod == 0 and (base+1) >= p and base != 0:
						counts += 1
						s -= 1
				else:
					if mod == 2 and base + 1 >= p:
						counts += 1
					elif mod != 2 and base + mod >= p:
						counts += 1			
		else:
			if mod != 2 and (base + mod) >= p:
				counts += 1
			elif (base + 1) >= p:
				counts += 1 

		if base < p - 2:
			break;
		"""
	print 'Case #' + str(i+1) + ': ' + str(counts)