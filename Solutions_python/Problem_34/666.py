import sys, re
from itertools import *

input = open(sys.argv[1], 'r')
L, D, N = map(int, input.readline().split())

content = input.readlines()
dictionary = content[:D]
cases = content[D:]

for idx,case in enumerate(cases):
	case = case.replace('(','[').replace(')',']')
	count = len(filter((lambda word: re.match(case, word)), dictionary))
	print "Case #%d: %d" % (idx+1, count)