#!usr/bin/env/python

from myFunctions import *
import time

problem = 'c'
s_input = 'small'
s_id = 'rn0'

'''
problem = 'a'
s_input = 'test'
s_id = '0'
'''
n, cases = parseInputData(problem, s_input, s_id)
result = ""
ta = time.time()
for i in range(0,n):
	result += "Case #%d: " %(i+1) + str((rec_nums1(cases[i]))) + '\n'
	
tb = time.time()
print (tb - ta)
writeOutput(result, problem, s_input, s_id)