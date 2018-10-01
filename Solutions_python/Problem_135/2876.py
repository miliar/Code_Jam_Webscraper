#! /usr/bin/python3

import sys

with open(sys.argv[1]) as test_file:
	lines = test_file.readlines()
	num_tests = int(lines[0])
	lines = lines[1:len(lines)]
	for i in range(num_tests):
		row1 = int(lines[0]) - 1
		config1 = [line.strip().split() for line in lines[1:5]]
		lines = lines[5:len(lines)]
		row2 = int(lines[0]) - 1
		config2 = [line.strip().split() for line in lines[1:5]]
		lines = lines[5:len(lines)]
		possible_nums = list(filter(lambda x: x in config1[row1], config2[row2]))
		if len(possible_nums) > 1:
			message = "Bad Magician!"
		elif len(possible_nums) == 0:
			message = "Volunteer cheated!"
		else:
			message = "{}".format(possible_nums[0])
		print("Case #{}: {}".format(i + 1, message))
