num_cases = int(input())

def is_tidy(val):
	digit_arr = [int(digit) for digit in str(val)]

	for i in range(len(digit_arr) - 1):
		if digit_arr[i+1] < digit_arr[i]:
			return False
	return True


def get_last_tidy(val):
	if val <= 9:
		return val
	
	digit_arr = [int(digit) for digit in str(val)]
	symbol_arr = [''] * len(digit_arr)
	num_minus = 0
	pos_first_eq = -1
	pos_first_minus = -1

	for i in range(1, len(digit_arr), 1):

		if digit_arr[i-1] < digit_arr[i]:
			symbol_arr[i] = "+"

		elif digit_arr[i-1] > digit_arr[i]:
			symbol_arr[i] = "-"
			num_minus += 1

			if pos_first_minus == -1:
				pos_first_minus = i

		else:
			symbol_arr[i] = "="

			if pos_first_eq == -1:
				pos_first_eq = i				

	if num_minus == 0:
		return val

	# handle case 2
	# go to last index before the consecutive ='s start
	curr_idx = pos_first_minus - 1
	
	if symbol_arr[curr_idx] == "=":
		while symbol_arr[curr_idx] == "=":
			curr_idx -= 1

	
	digit_arr[curr_idx] = digit_arr[curr_idx] - 1
	curr_idx += 1
	
	while curr_idx < len(digit_arr):
		digit_arr[curr_idx] = 9
		curr_idx += 1
	

	return int(''.join(map(str,digit_arr)))

# case 1	
# +-:		parse left to right, if a non = digit preceeds first - digit, then decrement previous digit then all digits after that are 9's
# 		if digit is a 0 while decrementing, change it to 9 and decrement its left digit by 1

# case 2 - special
# ====-:	if there are = digits just before first - is found, decrement the digit before the first = occurence, then all digits after that are 9's
# 		else ignore



for i in range(num_cases):
	val = int(input())
	result = get_last_tidy(val)

	
	print("Case #%d: %s" %(i + 1, result))
