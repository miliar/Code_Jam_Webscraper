NAME_IN = 'A-small-practice.in'
NAME_OUT = 'A-small-practice.out'

def read_input(name_of_file = NAME_IN):
	with open(name_of_file, 'r') as file_desc:
		file_data = file_desc.read()
	a = file_data.split('\n');
	number_of_strings = a[0]
	data = a[1:-1]
	return (number_of_strings,data)

def write_output(data, name_of_file = NAME_OUT):
	with open(name_of_file, 'w') as file_desc:
		for number_of_case, value in enumerate(data):
			output = f"Case #{number_of_case+1}: {value}\n"
			file_desc.write(output)
			