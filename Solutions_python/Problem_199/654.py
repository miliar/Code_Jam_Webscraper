#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam XXXX
Qualification Round
Problem A
Oversized Pancake Flipper

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* initial observations:
		* if all pancakes are initially +, answer is 0
		* else if len(S) < K, it's IMPOSSIBLE
		* else if len(S) < 2K and 2K - len(S) pancakes in the middle are not the same value, it's IMPOSSIBLE
		* else it's definitely possible?... nope... probably not guaranteed still
	* working out an algorithm:
		* can we simply move from left to right?
		* if the leftmost is -, it will definitely be necessary to flip in the 1st position
			* order of the flips doesn't matter
				* so there's no benefit to doing a necessary flip later rather than immediately
			* flipping an even number of times in a given position is the same as flipping 0 times, so it's never useful to flip more than once in a given position
		* if the 2nd from the left is - *after* ensuring the left is +, then it will definitely be necessary to flip the 2nd from the left
		* so... it seems that working from left to right is an optimal strategy
			* this is also what we'd expect from a problem A in the qualification round
		* once you've hit the rightmost flipping position, and determined whether to flip or not...
			* either they will all be +, or they won't be
			* if they are, we simply report the number of flips
			* if they aren't, we report IMPOSSIBLE
		* pretty simple
	* 

'''

################################################################################

import re

def read_case(id, input):
	# read test case from input
	
	S, sK = input.readline().split()
	K = int(sK)
	
	assert(not re.search(r'[^\+\-]', S))
	assert(2 <= K <= len(S))
	
	case = S, K
	
	return case

def solve_case(id, case):
	S, K = case
	
	S = list(S)  # turn the immutable string into a mutable list
	
	flips = 0
	
	for i in range(0, len(S) - K + 1):
		if S[i] == '-':
			flips += 1
			for j in range(i, i + K):
				S[j] = '-' if S[j] == '+' else '+'
	
	S = ''.join(S) # back to a string
	
	solution = 'IMPOSSIBLE' if re.search(r'-', S) else flips
	
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

