import re
import sys
import math

in_file = sys.argv[1]
input_file = open(in_file, 'rb')
output_file = open(in_file+'_output.txt', 'w+')

num_cases = int(input_file.next())
cases = []

def is_palindrome(x):
	x = str(x)
	for i, c in enumerate(reversed(x)):
		if x[i] != c:
			return False
	return True

def is_square(x):
	f = int(math.floor(math.sqrt(x)))
	f2 = int(f*f)
	while f2 <= x:
		if f2 == x:
			return True
		else:
			f += 1
			f2 = int(f*f)
	return False

def sqrt(x):
	return int(math.sqrt(x))

def find_num(a, b):
	a = int(a)
	b = int(b)
	count = 0
	first_square = None
	i = a
	while i <= b:
		if is_square(i):
			first_square = i
			if is_palindrome(i) and is_palindrome(sqrt(i)):
				count += 1
			break
		i += 1

	if first_square is None:
		return count

	j = sqrt(first_square) + 1
	k = j * j
	while k <= b:
		if is_palindrome(k) and is_palindrome(j):
			count += 1
		j += 1
		k = j * j

	return count

for i in range(num_cases):
	line = input_file.next()
	a, b = line.split()
	cases.append(find_num(a, b))


for i, result in enumerate(cases):
	output_file.write("Case #%d: %s" % (i+1, result) + "\n")