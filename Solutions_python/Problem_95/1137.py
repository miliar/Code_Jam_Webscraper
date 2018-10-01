#! /usr/bin/env python

#imports here
from myFunctions import *

##########################################################################################################################
# Main code goes here
					
problem = 'A'
s_input = 'small'
s_id = 'sit'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []

myDict = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

for i in range(nCase):
	result.append("Case #%d: %s\n" %(i+1, tongues(inputList[i], myDict)))

writeOutput(result, problem, s_input, s_id)

##########################################################################################################################
