#! /usr/bin/env python

#imports here
from myFunctions import *

##########################################################################################################################

# Main code goes here
					
problem = 'B'
s_input = 'large'
s_id = 'cookie'

first, rest = parseInputData_gen(problem, s_input, s_id)
N = StrToNum(first)
cases = map(StrTofloatList, rest)

result = []

for i in range(N):
	result.append("Case #%d: %s\n" %(i+1, cookie_clicker(cases[i])))

writeOutput(result, problem, s_input, s_id)

##########################################################################################################################5

