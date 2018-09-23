import sys


def main():
	sys.stdin = open('input.txt', 'r')
	sys.stdout = open('output.txt', 'w')

	T = int(input())
	for x in range(1, T + 1):
		N = int(input())
		y = greatest_tidy(N)
		print(f'Case #{x}: {y}')

		
def greatest_tidy(upper_bound):
	n = upper_bound
	while True:
		n2 = decrement(n)
		if n == n2:
			return n
		else:
			n = n2


def decrement(n):
	digits = list(map(int, str(n)))
	
	i = len(digits) - 1
	previous_digit = digits[i]
	i -= 1
	while i >= 0:
		current_digit = digits[i]
		if current_digit > previous_digit:
			digits[i] -= 1
			
			if digits[i] < 0:
				print('shit is wrong')
				sys.exit(1)
			
			j = i + 1
			while j < len(digits):
				digits[j] = 9
				j += 1
			
			break
		else:
			previous_digit = current_digit
		i -= 1
	
	return int(''.join(map(str, digits)))


if __name__ == '__main__':
	main()