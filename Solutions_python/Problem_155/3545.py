#simple program to create a standing ovation :D

input_file = open ('A-small-attempt0.in')
output_file = open ('output_file', 'w')
no_of_cases = int (input_file.readline().rstrip())

def get_people_required (people_list):
	no_of_people_required = 0
	no_of_people_present = 0
	shyness = -1

	for each_position in people_list:
		shyness += 1

		if no_of_people_present <= shyness:
			no_of_people_required += (shyness - no_of_people_present)
			no_of_people_present += (shyness - no_of_people_present)

		no_of_people_present += each_position

	return no_of_people_required

def process_input (input_string):
	people_list = list (input_string)
	
	index = 0
	for each_value in people_list:
		#debug! something is wrong here!
		people_list[index] = int (each_value)
		index += 1

	return people_list

for x in range (0, no_of_cases):
	people_string = input_file.readline().rstrip()

	if int (people_string[0]) < 0 or int (people_string[0]) > 6:
		pass

	else:
		print (people_string)
		people_list = process_input (people_string[2:])

		no_of_people_required = get_people_required (people_list)

		output = 'Case #' + str (x+1) + ': ' + str (no_of_people_required) + '\n'
		output_file.write (output)