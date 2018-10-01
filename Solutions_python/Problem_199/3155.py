def parse_case(input_string):
	tokens = input_string.split(" ")
	pancake_string = tokens[0]
	flipper_size = int(tokens[1])
	pancake_status = []
	for pancake in pancake_string:
		if pancake == '+':
			pancake_status.append(True)
		elif pancake == '-':
			pancake_status.append(False)
	return pancake_status, flipper_size

def generate_output(case, flips):
	result = "Case #" + str(case) + ": "
	if flips == -1:
		result += "IMPOSSIBLE"
	else:
		result += str(flips)
	return result

def is_finished(pancake_status):
	return sum(pancake_status) == len(pancake_status)

def flip_them_pancakes(pancake_status, position, flipper_size):
	new_status = pancake_status[:]
	for i in range(position, flipper_size + position):
		new_status[i] = not pancake_status[i]
	return new_status

def run_solution(possible_states, level, flipper_size, unique_states):
	if len(possible_states) == 0:
		return -1
	for state in possible_states:
		if is_finished(state):
			return level
	new_states = []
	for state in possible_states:
		for i in range(0, len(state) - flipper_size + 1):
			new_pancakes = flip_them_pancakes(state, i, flipper_size)
			tupled_pancakes = tuple(new_pancakes)
			if tupled_pancakes not in unique_states:
				unique_states.add(tupled_pancakes)
				new_states.append(new_pancakes)

	return run_solution(new_states, level + 1, flipper_size, unique_states)

def solve_case(pancake_status, flipper_size):
	possible_states = [pancake_status]
	level = 0
	unique_states = set()
	unique_states.add(tuple(pancake_status))
	return run_solution(possible_states, level, flipper_size, unique_states)

with open("A-small-attempt1.in", "r") as dataset:
	nb_cases = dataset.readline().rstrip("\n")
	input_cases = [line.rstrip('\n') for line in dataset.readlines()]

output_result = []
for case_nb,case in enumerate(input_cases):
	pancake_status, flipper_size = parse_case(case)
	flips_needed =  solve_case(pancake_status, flipper_size)
	output_result.append(generate_output(case_nb + 1, flips_needed))

with open("result.txt", "w+") as output_file:
	for line in output_result:
		output_file.write(line + "\n")
