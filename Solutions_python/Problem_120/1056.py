#! /usr/bin/env python
import math
#imports here
def parseInputData(problem, s_input, s_id):
	finput = open(problem + '-' + s_input + '-' + s_id + '.in','r')
	nCase = int(finput.readline().strip())
	inputList = finput.readlines()	
	finput.close()
	return nCase, inputList

##########################################################################################################################

def writeOutput(result, problem, s_input, s_id):
	foutput = open(problem + '-' + s_input + '-' + s_id + '.out','w')
	foutput.writelines(result)
	foutput.close()
	
def StrToNumList(s):
	#return [int(x) for x in re.findall('[0-9\-]+',s)]
	return [int(x) for x in s[:-1].split()]



def solve_bullseye(r, t):

	b = 0.5 - r
	c = -(t/2.0)

	if c < (b*b)/4.0:
		root1 = -b/2.0 + math.sqrt(b*b - 4*c)/2.0
		root2 = -b/2.0 - math.sqrt(b*b - 4*c)/2.0
	else:
		return 1

	root = int(max(-root1, -root2))
	if root > 1:
		return root
	else:
		return 1

##########################################################################################################################
# Main code goes here
					
problem = 'a'
s_input = 'small'
s_id = 'beye'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []
rownum = 0



for i in range(nCase):
	r, t = StrToNumList(inputList[rownum])
	result.append("Case #%d: %s\n" %(i+1, solve_bullseye(r, t)))
	rownum += 1
writeOutput(result, problem, s_input, s_id)



		




		

