#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Qualification Round
Problem B
Tidy Numbers

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* seems to involve huge numbers - python will handle it
	* *might* keep them as strings regardless of python's ability to handle huge numbers - we'll see what operations we need
	* very simple input space... though still a very large range - consider precalculation
	* given a number, we should be able to follow some rules to derive the closest tidy number preceding it
	* these rules could operate on base 10 digits, rather than integers
		* it may be that to handle the large dataset, we can't really afford to count 1-by-1
	* the most recent digit to change would have been the ...
	* remember: non-decreasing order
	* considering examples:
		* 123 - 123
		* 321 - 
	* some observations:
		* the most significant digit never has to reduce by more than 1
			* so it may be the original value, or the original value minus 1
		* note that it may reduce to 0, which means it won't be the most significant digit anymore
	* we consider digits that may be decreased, beginning with the least significant
	* but the only purpose in decreasing a digit, is to allow the digits to the right to increase to 9s
	* and that immediately solves the problem for all digits to the right, since 9 must be greater than or equal to any other digit
	* so... what we're really looking for is the leftmost pair of digits where the value decreases
	* we can fix this by decreasing the leftmost digit of the pair, by 1 - all digits to the right of it will then become 9s
	* but this may cause that digit to decrease with respect to the digit to its left
	* so we just have to keep moving left and so long as the left digit is bigger, decrease it and set all digits to the right to 9s
	* we don't have to change the digits to the right immediately - just note the leftmost position so far that the 9s extend to, and change the values in a later pass
	* so this should be O(N)
	* it may simplify things to reverse the string so array index is significance
	* note that we never have to decrease 0, as there is no digit less than 0, so we can't be decreasing from 0

'''

################################################################################


def read_case(id, input):
	N = input.readline().strip()
	
	assert(len(N) <= 19)
	
	case = N
	return case

def solve_case(id, case):
	N = case
	
	#digits = [ N[len(N) - i - 1] for i in range(len(N)) ]
	digits = [ int(digit) for digit in N ]
	
	i = len(digits) - 1
	nines = len(digits)
	while i > 0:
		if digits[i-1] > digits[i]:
			# decreasing - we need to fix it
			nines = i
			digits[i-1] -= 1
		i -= 1
	
	# form result with nines set
	solution = [ (9 if i >= nines else digits[i]) for i in range(len(digits)) ]
	
	# trim possible leading zero (more than 1 should be impossible
	if solution[0] == 0:
		solution = solution[1:]
	
	# convert back to string
	solution = ''.join( str(digit) for digit in solution )
	
	return "Case #{}: {}\n".format(id, solution)


def prepare():
	def prepare_data():
		return None
	
	global prepared_data
	prepared_data = prepare_cached(prepare_data, 'prepared_data.cached')


################################################################################


from sys import stdin, stdout, stderr
import time
import math
import pickle
import io

execution_timer = time.time
#execution_timer = time.clock
debugging = 1


################################################################################


def debug(message):
	if debugging:
		stderr.write(message() if hasattr(message, '__call__') else message)

def report(message):
	stderr.write(message)

def prepare_cached(prepare_data, pickle_path='data.pickle'):
	try:
		data = pickle.load(io.open(pickle_path, 'rb'))
		report("Loaded {}.\n".format(pickle_path))
	except IOError:
		data = prepare_data()
		report("Prepared {}.\n".format(pickle_path))
		pickle.dump(data, io.open(pickle_path, 'wb'))
	return data

def main():
	t0 = execution_timer()
	#prepare()
	t1 = execution_timer()
	report("Completed preparation in {:.6f} seconds.\n".format(t1 - t0))
	
	T = int(stdin.readline())
	for case_id in range(1,T+1):
		report("Processing test case {} of {} (output {}). {:.0f} seconds elapsed.".format(case_id, T, case_id-1, execution_timer() - t1))
		report("\n" if debugging else "\r")
		stderr.flush()
		stdout.write(solve_case(case_id, read_case(case_id, stdin)))
		stdout.flush()
	
	t2 = execution_timer()
	report("Processed {} test cases in {:.6f} seconds.                           \n".format(T, t2 - t1))
	report("Total time: {:.6f} seconds.\n".format(t2 - t0))

if __name__ == '__main__':
	main()

