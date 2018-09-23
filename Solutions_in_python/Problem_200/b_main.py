def solve_case(num):
	num_str = str(long(num))
	num_list = []
	for digit in num_str:
		num_list.append(int(digit))
	if len(num_str) == 1:
		return num_str

	for i in range(len(num_list))[-1:0:-1]:
		if num_list[i] < num_list[i-1]:
			for j in range(i, len(num_list)):
				num_list[j] = 9
			num_list[i-1] -= 1

	if num_list[0] == 0:
		num_list = num_list[1:]
	num_out = long(''.join(str(digit) for digit in num_list))

	return str(num_out)