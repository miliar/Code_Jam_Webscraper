from __future__ import print_function
import sys
import time
import math

def read_file(fn):
	with open(fn) as f:
		cont = f.readlines()
	print("Read input file \"" + fn + "\" successfully!")	
	return [line.strip().split(" ")  for line in cont]

def handle_input(fc, out_name):
	output_file = open(out_name, 'w')
	print("Opened output file \"" + out_name + "\" successfully!")
	test_cases_count = int(fc[0][0])
	
	counting_index = 1
	for test_index in range(1, test_cases_count + 1):
		print("Case #" + str(test_index) + "... ", end = '')

		next_length = int(fc[counting_index][1]) + 1
		result = handle_line(fc[counting_index:counting_index + next_length])
		
		counting_index += next_length
		output_file.write("Case #" + str(test_index) + ": " + result + "\n")
		print("Done")
	output_file.close()
	return

def handle_line(lines):
	D = int(lines[0][0]) + 0.0
	N = int(lines[0][1])


	max_time = 0
	for line in lines[1:]:
		Ki, Si = int(line[0]), int(line[1])
		to_travel = D - Ki
		speed_double = Si + 0.0
		time_to_travel = to_travel / speed_double
		if time_to_travel > max_time:
			max_time = time_to_travel
	return str(D/max_time)



if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Not enough args!")
	else:
		input_name = sys.argv[1]
		file_cont = read_file(input_name)	

		output_name = input_name[:input_name.index(".")] + ".out"
		handle_input(file_cont, output_name)	

