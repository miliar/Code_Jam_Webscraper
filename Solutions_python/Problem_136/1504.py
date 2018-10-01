def split_line(line, sep=' '):
	numbers = []
	num = ''

	for char in line:
		if char == sep:
			if num != '':
				numbers.append(float(num))
			num = ''
		else:
			num += char

	if num != '':
		numbers.append(float(num))
	num = ''

	return numbers

if __name__ == '__main__':
	f = open('in.in', 'r')#Open input file

	out = open('out.out', 'w')#Open output file

	test_cases = int(f.readline().strip())# Get number of test cases
	

	for n in xrange(1, test_cases+1):

		values = split_line(f.readline().strip())
		production_rate = 2#How quickly you get cookies
		secs = 0#Actual secs

		optimum_secs = 0

		while True:
			before_farm = secs + values[2] / production_rate

			secs += values[0] / production_rate #Seconds to buy farm
			production_rate += values[1]

			after_farm = secs + values[2] / production_rate

			if before_farm < after_farm:
				optimum_secs = before_farm
				break

		case = 'Case #{0}: {1}\n'.format(n, optimum_secs)
		out.write(case)