def get_test_cases():
	n = int(raw_input())
	for i in range(n):
		majorant_number = raw_input()
		yield majorant_number


def write_output(i, output):
	print "Case #{index}: {result}".format(index=i, result=output)


def change_to_nines(result, pos):
	for i in range(pos):
		result[i] = '9'


def solve(majorant_number):
	majorant_digits = map(int, list(str(majorant_number)))
	result = [0] * len(majorant_digits)
	max_digit = 10
	for i, digit in enumerate(majorant_digits[::-1]):
		if digit <= max_digit:
			max_digit = digit
			result[i] = str(digit)
		else:
			change_to_nines(result, i)
			result[i] = str(digit - 1)
			max_digit = digit - 1
	return int(''.join(result[::-1]))


def main():
	for i, input_data in enumerate(get_test_cases(), start=1):
		write_output(i, solve(input_data))


if __name__ == '__main__':
	main()