#!/usr/bin/env python3
#coding=UTF-8

'''

Google Code Jam 2017
Qualification Round
Problem C
Bathroom Stalls

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* the small dataset should be easy enough to solve by simulation, processing each person in turn according to the rules, to calculate the result for the final person
	* the large dataset is very very large, and perhaps will require a formula to jump directly to a result, with runtime independent of input size
	* the integer nature of the calculations may make a clean continuous formula invalid (eg. you have to pick one stall or the one next to it, not half-way between them)
	* but if we assume for a moment that everything was in powers of 2 (N, K)...
		* the first person halves the space, the next 2 divide it into quarters, the next 4 into eighths, etc...
		* actually, it would have to be ermm.. powers of 2 plus 1... like... you take 1 stall...
			* then double it and add 1, to get 3, with 1 in the dead center
			* then you double that and add 1 to get 7, with 1 in the dead center, and so on
	* so let's get clear on what we're calculating:
		* "When the last person chooses their stall S, what will the values of max(LS, RS) and min(LS, RS) be?"
			* does this mean, what will those values be *before* they choose their stall? or *after*?
			* I guess I need to check the sample input and output...
			* it's asking for the values of the stall actually chosen last
			* or... the values chosen by the last person in their decision process, I guess?
	* I think this problem can be expressed in a way that is significantly easier to understand and visualise:
		* people want to pick the leftmost largest available space, then pick the leftmost midpoint of that
		* and the answer is then the number of empty stalls to the left and right of the final chosen stall(biggest first)
		* I'm *almost* certain this is a correct re-expression of the problem
			* 2 spaces differing by 1 stall in size could have the same minimum distance to closest stall, but they would not also have the same maximum
			* the one with the smallest size overall would have the smallest maximum
		* I'm not certain if it really does make it easier though
	* let's consider this further...
		* when a person sits, they divide the space they choose into 2 parts, of either the same size, or off by 1
		* so they effectively replace that space with 2 spaces of those sizes
		* they always pick the larger space available...
		* so you could list spaces as a queue, ordered by size, biggest to smallest
		* so first, you have 1 space of size N
		* then after 1 person, you have 2 spaces of size (N-1)/2
		* then after 2 more people, you have 4 spaces of size (((N-1)/2)-1)/2
		* but of course this is glossing over the fact that the sizes must be integral, a rule which introduces inequality between the sizes
		* does this rule break down at any point, eg. where the larger size of one subdivision can be equal to the smaller size of the previous subdivision?
		* or do we *always* iterate over all spaces from 1 generation before we begin populating those of the next?
		* okay... when we have a bunch of spaces of size 1 and 2, the 2-size spaces will be filled first
			* at least some of the 2-size spaces may be to the right of a 1-size space, as we prefer to fill the space on the left, leaving more on the right
			* X.1..1.1..X - 1st generation - leaves 4 2nd-generation spaces
			* X.12.1.12.X - 2nd generation spaces being filled
			* X312.1.12.X - still filling 2nd-generation spaces
			* X31231.12.X - but now we're filling a 3rd-generation space, before the 2nd-generation is finished
			* X312313123X
			* so... trying to use a log-based approach which treats each "generation" distinctly is probably going to run into problems - in proof if not in practice
	* considering an approach:
		* at any given stage, we have a number of spaces of specific sizes
		* larger sizes will always fill before smaller sizes
		* the number of distinct sizes at any time is limited (I think to 3?)
			* proof?
				* we begin with 1 size
				* that may produce 2 distinct sizes after splitting
				* 
		* we can store this info as just a few size/quantity pairs
			* actually, we'll probably use a dict mapping from size to quantity
		* and we can divide an entire set of sizes in 1 step, if we have enough people
		* spaces of size 0 can be eliminated completely
		* to process a row:
			* check the number of people is as large as the number of spaces
				* if not, we handle termination of the calculation
			* calculate a smaller and larger space size for the resulting spaces
			* for each of these sizes which is not 0, add our original row size to the rows of that size
		* what's the complexity of this?
			* well, if we assume the 2 sizes are always the same, then it's log N
				* log2(10**18) is about 60?
			* then if we don't assume the 2 sizes are always the same, but do assume (probably true) that there is a fixed maximum number of sizes at any stage...
			* then that is effectively multiplication by a constant, leaving us with log N complexity still
			* we'll use python's large number support from the beginning - I don't think it will be a problem
			* note that we can speed-test the largest problem sizes (maybe the top 100 numbers) before even downloading anything
	* considering cases:
		* if a space is odd, it divides into 2 equal spaces (which may be odd or even)
		* if a space is even, it divides into an even and an odd space (either of which may be the smaller one)
		* considering a pair of spaces:
			* a smaller even space x and a larger odd space x+1:
				* x/2, x/2-1, x/2, x/2  -- 2 distinct sizes, 1 unit apart
			* a smaller odd space x and a larger even space x+1:
				* (x-1)/2, (x-1)/2, (x-1)/2+1, (x-1)/2  -- 2 distinct sizes, 1 unit apart
		* it seems that this kind of consideration may lead into proof of a limited number of distinct sizes at any given time
	
	* I wrote a solution which worked for the sample data
	* I created a stress test data file, using the largest 100 numbers in the large dataset range
		* running the stress test, it's clear we won't have speed issues with this algorithm
		* but it did reveal some deficiencies in my code
		* it actually crashed on test 65, due to the stalls running out
		* and I'm also questioning whether the answers for prior cases are correct... although... actually they probably are
			* they're all 0 0
			* which makes sense, since until we go down below half of the number of stalls, the last person will always be filling a gap of size 1
			* I also note that the number of distinct sizes doesn't go above 3
		* I think my error was failing to remember that python's accurate large number handling only extends to integers
			* for floating point, it has finite precision and is probably uses the system's double-precision type directly
		* so I just need to eliminate the fp division by 2
		* I guess I need floordiv and ceildiv operations?
		* okay, done and it seems to work fine and plenty fast enough
	

'''

################################################################################

from collections import defaultdict

def read_case(id, input):
	stalls, people = [ int(n) for n in input.readline().split() ]
	return stalls, people

def dump(f):
	def df(a, b):
		c = f(a, b)
		print('{}: {} / {} = {}'.format(f.__name__, a, b, c))
		return c
	return df

def div_floor(a, b):
	floor = a // b
	return a // b # we're only dealing with positive numbers for now, so... this will do

def div_ceil(a, b):
	floor = div_floor(a, b)
	if floor * b == a:
		return floor
	else:
		return floor + 1

def get_sizes(stalls, people):
	max_distinct_sizes = 0
	spaces = defaultdict(lambda: 0)
	spaces[stalls] = 1
	while True:
		distinct_sizes = len(spaces)
		assert(distinct_sizes > 0)
		max_distinct_sizes = max(distinct_sizes, max_distinct_sizes)
		
		# pick biggest space
		size = max(spaces.keys())
		
		small = div_floor(size - 1, 2)
		large = div_ceil(size - 1, 2)
		
		quantity = spaces[size]
		
		if people <= quantity:
			people = 0
			#print('max distinct sizes: {}'.format(max_distinct_sizes))
			return large, small
		else:
			del spaces[size]
			for newsize in small, large:
				if newsize > 0:
					spaces[newsize] += quantity
			people -= quantity

def solve_case(id, case):
	stalls, people = case
	
	large, small = get_sizes(stalls, people)
	
	return "Case #{}: {} {}\n".format(id, large, small)


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

