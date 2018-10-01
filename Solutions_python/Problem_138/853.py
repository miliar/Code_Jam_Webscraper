#! /usr/bin/env python

#imports here
from myFunctions import *

##########################################################################################################################

# Main code goes here
					
problem = 'D'
s_input = 'large'
s_id = 'war'

first, rest = parseInputData_gen(problem, s_input, s_id)
N = StrToNum(first)
cases = map(StrTofloatList, rest)

result = []

for i in range(N):
	result.append("Case #%d: %s\n" %(i+1, deceitful_war(cases[i*3:3*(i+1)])))

writeOutput(result, problem, s_input, s_id)

##########################################################################################################################5

