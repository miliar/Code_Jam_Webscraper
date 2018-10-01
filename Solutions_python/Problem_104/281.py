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
				write_case(fo, case_num, answer)

################################################################################

def read_case(f):
	line = read_ints(f)
	return ( line[1:] )


def write_case(f, case_num, answer):
	f.write("Case #{}: {}\n".format(case_num, answer))

################################################################################

def solver(case):
	superset = sorted(case)
	
	# Pick an element and find a subset that matches it
	for outer_len in range(1,len(superset)):
		for target in itertools.combinations(superset, outer_len):
			s = sum(target)
			for length in range(1,len(target)): # no point looking at sets with more elements
				#logging.debug("length: {}, testset: {}".format(length, superset[:i+2]))
				for c in itertools.combinations(superset, length):
					#logging.debug("e:{}, c: {}, sum: {}".format(e,c, sum(c)))
					if sum(c) == s:
						logging.debug("candidate! target: {}, c: {}".format(target,c))
						if target != c:
							# Success!
							return "\n{}\n{}".format(" ".join(map(str,target))," ".join(map(str,c)))
	return "\nImpossible"
		

################################################################################

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
solve(sys.argv[1])
