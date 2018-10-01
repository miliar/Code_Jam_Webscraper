import numpy as np
def mainFunc(R, C):	
	ret = ""
	M = np.chararray((R))
	M = np.chararray(M.shape, itemsize=C)
	M[:]=''
	init = -1
	for i in range(R):	
		P = raw_input()
		lc = '?'
		for j in range(C):
			if(P[j]!='?'):
				if(lc=='?'): M[i]=M[i].replace('?',P[j]) 
				lc = P[j]
			M[i]+=lc
		if (lc == '?'):	M[i] = M[i-1]
		elif(init<0): init = i
	for i in range(R):
		if (i<init): ret+="\n"+M[init]
		else: ret+="\n"+M[i]
	return str(ret)
		
T = int(raw_input())
for t in range(T):
	P = raw_input().split(' ')
	print 'Case #' + str(t+1) + ': ' +	mainFunc(int(P[0]), int(P[1]))