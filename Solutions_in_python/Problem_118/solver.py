from functions import *
import math


def solve(puzzle_input):
	(num_testcases, testcases) = parse_2_input(puzzle_input)
	for testcase in testcases:
		output = solve_range(int(testcase[0]),int(testcase[1]))
		write_output(output)

	flush_output()

def test():
	for i in range(10,32):
		if verify_palindrome(i) and verify_palindrome(i*i):
			print str(i) + ' | ' + str(i * i)




def solve_range(lower_limit, upper_limit):
	print 'solving range ' + str(lower_limit) + ' to ' + str(upper_limit)
	palindrome_lower = int(math.ceil(math.sqrt(lower_limit)))
	palindrome_upper = int(math.floor(math.sqrt(upper_limit)))
	count = 0
	for palindrome in generate_palindromes(palindrome_lower, palindrome_upper):
		#print 'checking ' + str(palindrome)
		square = palindrome * palindrome
		#print '\t' + str(square)
		if verify_palindrome(square):
			count += 1

	return count

def verify_palindrome(i):
	if int_len(i) == 1:
		return True
	return first_half(i) == second_half_reversed(i)

def generate_palindromes(lower, upper):
	for i in range(int_len(lower), int_len(upper) + 1):
		if i == 1:
			for j in range(10):
				if j >= lower and j <= upper:
					yield j
		else:
			lowest = int(pow(10, math.floor(i/2.0) - 1))
			highest = int(pow(10, math.floor(i/2.0)))


			if int_len(lower) == i:
				lowest = first_half(lower)
				if second_half_reversed(lower) > first_half(lower):
					lowest += 1

			if int_len(upper) == i:
				highest = first_half(upper) + 1
				if second_half_reversed(upper) < first_half(upper):
					highest -= 1


			if i % 2 == 0:
				# even
				for j in range(lowest, highest):
					yield int(str(j) + str(j)[::-1]) ## convert into palindrome
			else:
				# odd
				for j in range(lowest, highest):
					yield int(str(j) + str(j)[0:-1][::-1]) ## convert into palindrome


def int_len(i):
	return len(str(i))

def first_half(i):
	j = int(math.floor(int_len(i)/2.0))
	return int(str(i)[:j])

def second_half_reversed(i):
	j = int(math.ceil(int_len(i)/2.0))
	return int(str(i)[j:][::-1])