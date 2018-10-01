import sys
import math

def is_palindrome(n):
	s = str(n)
	s_reversed = s[::-1]
	return (s == s_reversed)
	
input = open(sys.argv[1], 'r')

n = input.readline()
n = n[:-1]
n = int(n)

for i in range(0, n):
	interval = input.readline().split()
	a = int(interval[0])
	b = int(interval[1])

	fair_and_square = 0
	
	for x in range(a, b + 1):
		if (is_palindrome(x)):
			sqrt_int = int(math.sqrt(x))
			if ((sqrt_int * sqrt_int == x) and is_palindrome(sqrt_int)):
				fair_and_square += 1

	sys.stdout.write('Case #' + str(i + 1) + ': ')	
	sys.stdout.write(str(fair_and_square))
	
	if (i + 1 < n):	
		print('')

input.close()