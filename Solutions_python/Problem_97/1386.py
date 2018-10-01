if __name__ == '__main__':
	input_file = open('C-large.in', 'r')
	output_file = open('C-large.out', 'w')
	
	test_cases_count = int(input_file.readline())
	
	for line_number in range(test_cases_count):
		line = input_file.readline()
		words = line.strip().split(' ')
	
		pairs = dict()
		a = int(words[0])
		b = int(words[1])
		
		for number in range(a, b+1):
			number_str = str(number)
			number_len = len(number_str)
			
			for i in range(1, number_len):
				if number_str[-i:].startswith('0'):
					continue
				
				new_number = int('%s%s' % (number_str[-i:], number_str[:number_len-i]))
				
				if new_number <= b and new_number > number:
					pairs['%d%d' % (number, new_number)] = 1
			
		output_file.write('Case #%d: %d\n' % (line_number+1, len(pairs.keys())))
		
	input_file.close()
	output_file.close()