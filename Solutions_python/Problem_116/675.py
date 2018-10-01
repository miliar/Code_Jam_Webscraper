#!usr/bin/env/python

# from myFunctions import *

##########################################################################################################################

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

##########################################################################################################################

def tttt_sol(X,O,nil_flag):
	winner = ''
	for i in range(4):
		if sum(X[i]) == 4:
			winner = 'X won'
			return winner
		if sum(O[i]) == 4:
			winner = 'O won'
			return winner

	for j in range(4):
		if X[0][j] + X[1][j] + X[2][j] + X[3][j] == 4:
			winner = 'X won'
			return winner
		if O[0][j] + O[1][j] + O[2][j] + O[3][j] == 4:
			winner = 'O won'
			return winner

	if X[0][0] + X[1][1] + X[2][2] + X[3][3] == 4:
		winner = 'X won'
		return winner

	if X[0][3] + X[1][2] + X[2][1] + X[3][0] == 4:
		winner = 'X won'
		return winner

	if O[0][0] + O[1][1] + O[2][2] + O[3][3] == 4:
		winner = 'O won'
		return winner

	if O[0][3] + O[1][2] + O[2][1] + O[3][0] == 4:
		winner = 'O won'
		return winner

	if nil_flag == True:
		return 'Game has not completed'

	return 'Draw'

##########################################################################################################################

def tttt_matrix(input):
	X = []
	O = []
	nil_flag = False
	for i in range(4):
		Xs = []
		Os = []
		for j in range(4):
			if input[i][j] == 'T':
				Xs.append(1)
				Os.append(1)
			elif input[i][j] == 'X':
				Xs.append(1)
				Os.append(0)
			elif input[i][j] == 'O':
				Xs.append(0)
				Os.append(1)
			else:
				Xs.append(0)
				Os.append(0)
				nil_flag = True
		X.append(Xs)
		O.append(Os)
	return X, O, nil_flag

##########################################################################################################################

problem = 'a'
s_input = 'large'
s_id = 'tttt'


# problem = 'a'
# s_input = 'test'
# s_id = '0'
rownum = 0

n, cases = parseInputData(problem, s_input, s_id)
result = ""
# for i in range(4,len(cases),5):
# 	X,O,nil_flag = tttt_matrix(cases[i-4:i])
# 	result += "Case #%d: " %((i/5)+1) + str((tttt_sol(X,O,nil_flag))) + '\n'

for i in range(n):
	X,O,nil_flag = tttt_matrix(cases[rownum:rownum+4])
	result += "Case #%d: " %(i+1) + str((tttt_sol(X,O,nil_flag))) + '\n'
	rownum+=5

writeOutput(result, problem, s_input, s_id)