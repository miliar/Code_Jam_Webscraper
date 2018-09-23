def are_happy(pancake_list):
	for pancake in pancake_list:
		if pancake == '-':
			return False
	return True

def flip(pancake_list, k, index):
	for i in range(index, index+k):
		if pancake_list[i] == '+':
			pancake_list[i] = '-'
		else:
			pancake_list[i] = '+'

	return pancake_list

def solve_case(case_in):
	input_list = case_in.split()
	pancake_str = input_list[0]
	k = int(input_list[1])
	pancake_list = []
	for pancake in pancake_str:
		pancake_list.append(pancake)

	if are_happy(pancake_list):
		return 0
	if k > len(pancake_list):
		return 'IMPOSSIBLE'

	num_flips = 0
	for i in range(0, len(pancake_list)-k+1):
		if pancake_list[i] == '-':
			pancake_list = flip(pancake_list, k, i)
			num_flips += 1

	if not are_happy(pancake_list):
		return 'IMPOSSIBLE'

	return num_flips