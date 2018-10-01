from __future__ import print_function
import sys

'''Four arrays with four members
A
B
C
D

xwins:
A[0-3] = 'X' or 'T'
B[0-3] = 'X' or 'T'
C[0-3] = 'X' or 'T'
D[0-3] = 'X' or 'T'
A-B[0] = 'X' or 'T'
A-B[1] = 'X' or 'T'
A-B[2] = 'X' or 'T'
A-B[3] = 'X' or 'T'
A[0] B[1] C[2] D[3] = 'X' or 'T'
A[3] B[2] C[1] D[0] = 'X' or 'T'

'''
XWin = ['X', 'T']
OWin = ['O', 'T']


def Winner(A,B,C,D):
	
	#cases where X wins
	if A[0] in XWin and A[1] in XWin and A[2] in XWin and A[3] in XWin:
		return 'X won'
	if B[0] in XWin and B[1] in XWin and B[2] in XWin and B[3] in XWin:
		return 'X won'
	if C[0] in XWin and C[1] in XWin and C[2] in XWin and C[3] in XWin:
		return 'X won'
	if D[0] in XWin and D[1] in XWin and D[2] in XWin and D[3] in XWin:
		return 'X won'
	if A[0] in XWin and B[0] in XWin and C[0] in XWin and D[0] in XWin:
		return 'X won'
	if A[1] in XWin and B[1] in XWin and C[1] in XWin and D[1] in XWin:
		return 'X won'
	if A[2] in XWin and B[2] in XWin and C[2] in XWin and D[2] in XWin:
		return 'X won'
	if A[3] in XWin and B[3] in XWin and C[3] in XWin and D[3] in XWin:
		return 'X won'
	if A[0] in XWin and B[1] in XWin and C[2] in XWin and D[3] in XWin:
		return 'X won'
	if A[3] in XWin and B[2] in XWin and C[1] in XWin and D[0] in XWin:
		return 'X won'
	#cases where Y wins
	if A[0] in OWin and A[1] in OWin and A[2] in OWin and A[3] in OWin:
		return 'O won'
	if B[0] in OWin and B[1] in OWin and B[2] in OWin and B[3] in OWin:
		return 'O won'
	if C[0] in OWin and C[1] in OWin and C[2] in OWin and C[3] in OWin:
		return 'O won'
	if D[0] in OWin and D[1] in OWin and D[2] in OWin and D[3] in OWin:
		return 'O won'
	if A[0] in OWin and B[0] in OWin and C[0] in OWin and D[0] in OWin:
		return 'O won'
	if A[1] in OWin and B[1] in OWin and C[1] in OWin and D[1] in OWin:
		return 'O won'
	if A[2] in OWin and B[2] in OWin and C[2] in OWin and D[2] in OWin:
		return 'O won'
	if A[3] in OWin and B[3] in OWin and C[3] in OWin and D[3] in OWin:
		return 'O won'
	if A[0] in OWin and B[1] in OWin and C[2] in OWin and D[3] in OWin:
		return 'O won'
	if A[3] in OWin and B[2] in OWin and C[1] in OWin and D[0] in OWin:
		return 'O won'
	#Game still going
	if '.' in A or '.' in B or '.' in C or '.' in D:
		return 'Game has not completed'
	else:
		return 'Draw'
		
		
def readFile(myFile):
	f = open(myFile)
	
	i = 0
	j = 1
	A,B,C,D = [],[],[],[]
	for line in f:
		if i==0:
			T = int(line)
			i += 1
		elif i==1:
			A = line
			i+=1
		elif i ==2:
			B = line
			i +=1
		elif i ==3:
			C = line
			i+=1
		elif i ==4:
			D = line
			i+=1
			print("Case #"+str(j)+": " + str(Winner(A,B,C,D)),sep='')
			j +=1
			i = 'blank'
		elif i == 'blank':
			i = 1

		

readFile(sys.argv[1])
