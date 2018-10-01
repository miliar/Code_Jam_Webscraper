import sys
import math

def sqrt(n):
	x = n
	y = (x + n // x) // 2
	while y < x:
		x = y
		y = (x + n // x) // 2
	return x
	
def palindrome(n):
	s = str(n)
	first_half = s[:int(math.floor(len(s)/2.0))]
	second_half = s[int(math.ceil(len(s)/2.0)):]
	return first_half == second_half[::-1]

def main():
	input = sys.argv[1]
	output = sys.argv[2]
	
	cases = 0
	ranges = []
	with open(input, 'r') as f:
		cases = int(f.readline())
		i = 0
		while i < cases:
			line = f.readline()
			split = line.split(' ')
			if len(split) < 2:
				break
			numbers = []
			for s in split:
				numbers.append(int(s))
			ranges.append(numbers)
			
	with open(output, 'w') as f:
		i = 1
		for r in ranges:
			fair_and_square = 0
			for n in range(r[0], r[1]+1):
				if (palindrome(n)):
					root = sqrt(n)
					if root**2 == n and palindrome(root):
						fair_and_square += 1
			f.write('Case #' + str(i) + ': ' + str(fair_and_square) + '\n')
			i += 1

if __name__ == '__main__':
	main()