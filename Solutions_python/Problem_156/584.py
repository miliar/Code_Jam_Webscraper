import math

LINES_FOR_EACH_INPUT = 2
INPUT_FILE_NAME = 'input.txt'
OUTPUT_FILE_NAME = 'output.txt'

def do_case(parsed_input):
	num_of_diners = parsed_input[0]
	cur_diners = parsed_input[1]
	
	return str(max(cur_diners) if max(cur_diners) <= 2 else min(min([sum([0 if diner <= tresh else ((diner - 1)/tresh) for diner in cur_diners]) + min(max(cur_diners), tresh) for tresh in range(1, max(cur_diners))]), max(cur_diners)))

def do_parse(input):
	return [int(input[0]), map(int,input[1].split(' '))]

def main():
	input_f = open(INPUT_FILE_NAME, 'r')
	output = []
	
	num_of_test_cases = int(input_f.readline(), 10)
	
	input_lines = input_f.readlines()
	
	for test_case in range(num_of_test_cases):
		parsed_input = do_parse(input_lines[test_case*LINES_FOR_EACH_INPUT : (test_case + 1) * LINES_FOR_EACH_INPUT])
		output.append('Case #' + str(test_case + 1) + ': ' + do_case(parsed_input))

	output_f = open(OUTPUT_FILE_NAME, 'w')
	output_str = '\n'.join(output)
	output_f.write(output_str)
	print output_str
	
	input_f.close()
	output_f.close()
	
if __name__ == '__main__':
	main()