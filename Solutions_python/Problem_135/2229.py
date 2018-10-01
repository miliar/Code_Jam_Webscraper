a =  open('A-small-attempt1.in')
num_cases = int(a.readline())

output_string = ""
case = "Case #"
bad_mage = "Bad magician!"
bad_vol = "Volunteer cheated!"

for i in range(num_cases):
	first_row_num = int(a.readline())
	first_arrange = ""
	for j in range(4):
		first_arrange += a.readline()
	first_arrange_array = first_arrange.split()

	second_row_num = int(a.readline())
	second_arrange = ""
	for k in range(4):
		second_arrange += a.readline()
	second_arrange_array = second_arrange.split()

	first_four_numbers = first_arrange_array[(first_row_num-1)*4:(first_row_num*4)]
	second_four_numbers = second_arrange_array[(second_row_num-1)*4:(second_row_num*4)]

	num_matches = 0
	for num1 in first_four_numbers:
		for num2 in second_four_numbers:
			if(num1 == num2):
				num_matches += 1
				winner = num1
	if(num_matches == 0):
		output_string += (case + str(i+1) + ": " + bad_vol + "\n")
	elif(num_matches == 1):
		output_string += (case + str(i+1) + ": " + str(winner) + "\n")
	else:
		output_string += (case + str(i+1) + ": " + bad_mage + "\n")

output = open('out.txt', 'w')
output.write(output_string)
output.close
a.close
