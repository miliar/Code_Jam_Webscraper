#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Round 1B
Problem A
Steed 2: Cruise Control

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* calculate time for annie to reach D
	* then calculate speed from that (D / time)
	* 

'''

################################################################################

class Horse:
	def __init__(self, start, speed):
		self.start = start
		self.speed = speed

def solve_case(id, case):
	D, N, horses = case
	
	def time(horse):
		distance = D - horse.start
		return distance / horse.speed
	
	maxtime = max( time(horse) for horse in horses )
	
	speed = D / maxtime
	
	solution = speed
	
	return "Case #{}: {}\n".format(id, solution)

def read_case(id, input):
	D, N = [int(n) for n in input.readline().split()]
	horses = []
	for i in range(N):
		K, S = [int(n) for n in input.readline().split()]
		horses.append(Horse(K, S))
	
	case = D, N, horses
	return case

def prepare_data():
	return None

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
		with io.open(pickle_path, 'rb') as file:
			data = pickle.load(file)
			report("Loaded {}.\n".format(pickle_path))
	except IOError:
		data = prepare_data()
		if data:
			report("Prepared {}.\n".format(pickle_path))
			with io.open(pickle_path, 'wb') as file:
				pickle.dump(data, file)
	return data

def prepare():
	global prepared_data
	prepared_data = prepare_cached(prepare_data, 'prepared_data.cached')

def main():
	t0 = execution_timer()
	prepare()
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

