import os

def solve(f_in):
	C, F, X = (float(elem) for elem in f_in.readline().split())

	time = 0.0

	current_speed = 2

	while X / current_speed > C / current_speed + X / (current_speed + F):
		time += C / current_speed
		current_speed += F

	time += X / current_speed

	return '%.7f' % time

if __name__ == "__main__":
	input_filename = 'B-large.in'
	output_filename = 'Qualification_ProblemB_Large_Output.txt'

	f_in = open(input_filename)
	counter = 0
	while os.path.isfile(output_filename):
		counter += 1
		output_filename = output_filename.split('.')[0] + str(counter) + '.txt'
	f_out = open(output_filename, 'a')

	test_cases = int(f_in.readline())
	
	for i in range(test_cases):
		ans = solve(f_in)
		f_out.write('Case #' + str(i + 1) +': ' + str(ans) + '\n')

	f_in.close()
	f_out.close()

	print 'Problem completed!'




