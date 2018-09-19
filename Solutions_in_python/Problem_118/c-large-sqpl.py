#! /usr/bin/env python

#imports here
import math

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


def gen_palindrome():
	p = range(1,4) #a
	p = p + [a + a*10 for a in range(1,4)] #aa
	p = p + [a+ b*10 + a*100 for a in range(1,4) for b in range(10)] #aba
	p = p + [a + b*10 + b*100 + a*1000 for a in range(1,4) for b in range(10)] #abba
	p = p + [a + b*10 + c*100 + b*1000 + a*10000 for a in range(1,4) for b in range(10) for c in range(10)] #abcba
	p = p + [a + b*10 + c*100 + c*1000 + b*10000 + a*100000 for a in range(1,4) for b in range(10) for c in range(10)] #abccba
	p = p + [a + b*10 + c*100 + d*1000 + c*10000 + b*100000 + a*1000000 for a in range(1,4) for b in range(10) for c in range(10) for d in range(10)] #abcdcba
	return p



def solve_palindrome(p, C, D):
	L = filter(lambda x: C <= x <= D, p)
	L = map(lambda x: x*x, L)
	L = filter(lambda x: str(x) == str(x)[::-1], L)
	return str(len(L))

##########################################################################################################################
# Main code goes here
					
problem = 'c'
s_input = 'large1'
s_id = 'sqpl'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []
rownum = 0

p = gen_palindrome()


for i in range(nCase):
	A, B = StrToNumList(inputList[rownum])
	C, D = math.sqrt(A), math.sqrt(B)
	result.append("Case #%d: %s\n" %(i+1, solve_palindrome(p, C, D)))
	rownum += 1
writeOutput(result, problem, s_input, s_id)









			




		




		

