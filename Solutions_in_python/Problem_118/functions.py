import os

puzzle_folder = 'qa'
output_buffer = ''
puzzle_output = ''
current_testcase = 1

def set_puzzle(puzzle='qa'):
	global puzzle_folder
	puzzle_folder = puzzle

def get_puzzle():
	return puzzle_folder

def set_output(output_file):
	global puzzle_output
	puzzle_output = output_file

def get_output():
	return puzzle_output

def write_output(output):
	global output_buffer
	global current_testcase
	if output is None:
		output = 'ERROR - NONE TYPE OUTPUT'
	output_buffer += 'Case #' + str(current_testcase) + ': ' + str(output) + '\n'
	current_testcase += 1

def flush_output():
	f = get_output()
	f.write(output_buffer)
	f.close()

def base_dir():
	return os.path.dirname(__file__)

def open_input(name="input"):
	filename = os.path.join(base_dir(), get_puzzle(), name)
	return open(filename).read()

def open_output(name="output"):
	filename = os.path.join(base_dir(), get_puzzle(), name)
	return open(filename, 'w+')

def parse_2_input(puzzle_input):
	lines = puzzle_input.split('\n')
	num_testcases = lines[0]
	lines.pop(0)
	testcases=[]
	for x in range(len(lines)):
		line = lines[x]
		line = line.split(' ')
		a = line[0]
		b = line[1]
		testcases.append((a,b))
	return (num_testcases, testcases)

