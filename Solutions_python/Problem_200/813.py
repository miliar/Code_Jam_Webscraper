def solve(n):
	cleaned = False
	digits = [i for i in str(n)]
	output = digits[0]
	for digit in digits[1:]:
		if cleaned:
			output += '9'
		elif digit >= output[-1]:
			output = output + digit
		else:
			output = cleanup(output)
			output += '9'
			cleaned = True
	return int(output)

def cleanup(n):
	cleanup_n = ''
	for digit, prev_digit in zip(reversed(n), reversed(n[:-1])):
		if digit == prev_digit:
			cleanup_n = '9' + cleanup_n
		else:
			cleanup_n = str(int(digit) - 1) + cleanup_n
			cleanup_n = n[:len(n) - len(cleanup_n)]	+ cleanup_n
			return cleanup_n
	cleanup_n = str(int(n[0]) - 1) + cleanup_n
	return cleanup_n

def is_tidy(n):
	digits = [i for i in str(n)]
	for digit, next_digit in zip(digits, digits[1:]):
		if digit > next_digit:
			return False
	return True

T = int(raw_input())
for t in range(1, T+1):
	print("Case #{0}: {1}".format(t, solve(int(raw_input()))))
