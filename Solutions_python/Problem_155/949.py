if __name__ == '__main__':
	T = int(raw_input())

	for i in xrange(0, T):
		input_line = raw_input().split()
		s_max = int(input_line[0])
		people_list = list(input_line[1])

		min_friends = 0
		total = 0
		if(people_list[0] == '0'):
			min_friends = 1
			total = 1

		for shyness_level, n_people in enumerate(people_list):
			if (total < shyness_level):
				min_friends += shyness_level - total
				total += shyness_level - total
			total += int(n_people)
			
		print "Case #%d: %d" %(i+1,min_friends)