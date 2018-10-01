import math

def get_cases(input_path):
	f = open(input_path)
	num_cases = int(f.readline().strip())

	test_cases = []
	curr_case = []
	for line in f:
		curr_case.append(line.strip())

		if len(curr_case) == 2:
			num_diners = int(curr_case[0])
			pancake_counts = [int(i) for i in curr_case[1].split(' ')]
			assert num_diners == len(pancake_counts)
			test_cases.append(pancake_counts)
			curr_case = []
	f.close()

	assert not curr_case
	assert num_cases == len(test_cases)
	return test_cases

def split_stacks(pancake_counts):
	max_value = max(pancake_counts) # split the largest stack

	if max_value > 1:
		# need to generalize later...
		if max_value == 9:
			half1 = max_value / 3 # floor
		else:
			half1 = max_value / 2 # floor
			
		half2 = max_value - half1

		index_of_max = pancake_counts.index(max_value)
		pancake_counts[index_of_max] = half1
		pancake_counts.append(half2)

		return pancake_counts

	# if max value less than 1, we can't split any more and
	# breakfast will be over next minute when we decrement
	else: 
		return []

def decrement_stacks(pancake_counts):
	return [i-1 for i in pancake_counts if i-1 > 0]

def choose(pancake_counts, memo):
	if not any(pancake_counts): # the breakfast has been terminated
		return 0

	# option 1: split each stack in half
	pancake_counts1 = split_stacks(pancake_counts[:]) # shallow copy list
	height1 = choose(pancake_counts1, memo)

	# option 2: decrement 1 from each diner
	pancake_counts2 = decrement_stacks(pancake_counts)
	height2 = choose(pancake_counts2, memo)
	
	return min(height1, height2) + 1

def solve(pancake_counts, memo):
	return choose(pancake_counts, memo)


if __name__ == '__main__':
	input_path = 'input.txt'
	output_path = 'output.txt'

	test_cases = get_cases(input_path)
	memo = {}

	print solve([1], memo)

	f = open(output_path, 'w')
	for (index, case) in enumerate(test_cases):
		print case
		print 'Case #%d: %s' % (index+1, solve(case, memo))
		print >> f, 'Case #%d: %d' % (index+1, solve(case, memo))
		print
	f.close()


