#! /usr/bin/env python

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
	

def ttt_check_sum(sqr, ident):
	A = []
	for i in range(4):
		B = []
		for j in range(4):
			if sqr[i][j] == ident or sqr[i][j] == 'T':
				B.append(1)
			else:
				B.append(0)
		A.append(B)

	for i in A:
		if sum(i) == 4:
			return 1

	for j in range(4):
		if A[0][j] + A[1][j] + A[2][j] + A[3][j] == 4:
			return 1

	if A[0][0] + A[1][1] + A[2][2] + A[3][3] == 4:
		return 1

	if A[0][3] + A[1][2] + A[2][1] + A[3][0] == 4:
		return 1


def ttt_solve_case(sqr):

	if ttt_check_sum(sqr, 'X') == 1:
		return 'X won'

	if ttt_check_sum(sqr, 'O') == 1:
		return 'O won'

	if ''.join(sqr).find('.') == -1:
		return 'Draw'
	else:
		return 'Game has not completed'

##########################################################################################################################
# Main code goes here
					
problem = 'A'
s_input = 'large'
s_id = 'ttt'

nCase, inputList = parseInputData(problem, s_input, s_id)
result = []
rownum = 0


for i in range(nCase):
	result.append("Case #%d: %s\n" %(i+1, ttt_solve_case(inputList[rownum:rownum+4])))
	rownum += 5

writeOutput(result, problem, s_input, s_id)

		




		

