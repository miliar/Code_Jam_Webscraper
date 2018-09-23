def reduce_digit(position, old_string):
	new_value = int(old_string[position]) - 1
	if new_value >= 0:
		return old_string[:position] + str(new_value) + old_string[position + 1:]
	else:
		return old_string

def max_digit(position, old_string):
	return old_string[:position] + "9" + old_string[position + 1:]

def is_tidy(nb_string):
	return list(nb_string) == sorted(nb_string)

def solve_case(limit_nb):
	string_limit = str(limit_nb)
	current_digit = len(string_limit) - 1
	current_string = string_limit
	while current_digit > 0:
		if is_tidy(current_string):
			return int(current_string)
		current_string = max_digit(current_digit, current_string)
		if(current_string > string_limit):
			current_string = reduce_digit(current_digit - 1, current_string)
		current_digit -= 1
	return int(current_string)


def generate_output(case, nb):
	return "Case #" + str(case) + ": " + str(nb)

with open("B-large.in", "r") as dataset:
	nb_cases = dataset.readline().rstrip("\n")
	output_result = []
	case_nb = 1
	for line in dataset:
		input_case = int(line.rstrip('\n'))
		last_nb =  solve_case(input_case)
		output_result.append(generate_output(case_nb, last_nb))
		case_nb += 1

	with open("result.txt", "w+") as output_file:
		for line in output_result:
			output_file.write(line + "\n")