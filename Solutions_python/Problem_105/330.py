import sys
import itertools
import math
import logging
from functools import partial

# CodeJam I/O helpers adapted from royf

# A single word (minus whitespace)
def read_word(f):
	return next(f).strip()

# A single int (given base)
def read_int(f, base=10):
	return int(read_word(f), base)

# A list of characters (including whitespace)
def read_letters(f):
	return list(read_word(f))

# A list of digits (whitespace results in error)
def read_digits(f, base=10):
	return [int(x, base) for x in read_letters(f)]

# A list of words split by whitespace
def read_words(f, delimiter=' '):
	return read_word(f).split(delimiter)

# A list of values interpreted by converter, split by delimiter
def read_values(f, converter, delimiter=' '):
	return [converter(x) for x in read_words(f, delimiter)]

# A list of ints split by whitespace
def read_ints(f, base=10, delimiter=' '):
	return read_values(f, partial(int,base=base), delimiter)

# Read 'length' lines, return a list interpreting each line using 'reader=read_ints'
# Use functools.partial to specify reader arguments
def read_arr(f, length, reader=read_ints):
	res = []
	for _i in range(length):
		res.append(reader(f))
	return res

def solve(fn, out_fn=None):
	in_fn = fn + '.in'
	if out_fn is None:
		out_fn = fn + '.out'
	with open(in_fn, 'r') as fi:
		with open(out_fn, 'w') as fo:
			T = read_int(fi)
			for case_num in range(1, T+1):
				case = read_case(fi)
				answer = solver(case)
				logging.info("Solved case {}".format(case_num))
				logging.debug("{}".format(answer))
				write_case(fo, case_num, answer)

################################################################################

def read_case(f):
	num_classes = read_int(f)
	classes = read_arr(f, num_classes)
	return ( classes )



def write_case(f, case_num, answer):
	f.write("Case #{}: {}\n".format(case_num, answer))

################################################################################

def solver(case):
	def diamond(start, end, path=[]): # uses global routes
		path = path + [start]
		if start == end:
			logging.debug("route found: {}".format(path))
			if ((path[0],end) in routes) and (routes[(path[0],end)] != path):
				return True
			else: # save the route
				routes[(path[0],end)] = path
				return False
		for node in classes[start]:
			if node not in path:
				if diamond(node, end, path):
					return True
		return False

		if s in routes:
			routes[s] += e
		else:
			routes[s] = e
		return False

	classes = []
	for c in case:
		classes += [[i-1 for i in c[1:]]]

	# For each class, it might form a start or end iff it has >=2 outs or ins
	starts = [i for i,c in enumerate(classes) if len(c)>=2]
	inputs = {}
	for c in classes:
		for link in c:
			if link in inputs:
				inputs[link] += 1
			else:
				inputs[link] = 1
	ends = [c for c in inputs.keys() if inputs[c]>=2]

	logging.debug("case: {}, starts: {}, ends: {}".format(classes,starts,ends))
	# keep track of what's possible
	routes = {}
	# Try every combination
	for s in starts:
		for e in ends:
			if e == s:
				break
			logging.debug("start: {}, end: {}".format(s,e))
			first = None
			if diamond(s, e):
				return "Yes"


	return "No"

################################################################################

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
solve(sys.argv[1])
