INPUT_FILE = "A-large.in"
OUTPUT_FILE = "A-large.out"

import math

global result
global caseNumber



def IsX(point):
	if point == 'X' or point == 'T':
		return True
	else:
		return False
		
def IsO(point):
	if point == 'O' or point == 'T':
		return True
	else:
		return False


def SolveA(P,Q):

	global result
	global caseNumber
	
	
	
	
	
	
	if (P>Q):
		result += "Case #%d: impossible\n" %(caseNumber+1)
		return


		
	if (Q%P == 0):
		Q = Q/P
		P = 1
	
	
	maxpow = 2**40
	
	
	if (P*maxpow%Q!=0):
		result += "Case #%d: impossible\n" %(caseNumber+1)
		return
		
		
	numP = P*maxpow/Q
	
	
	poww = 1
	for j in xrange(40):
		
		i = j+1

		poww *= 2;
		frac = 1.0/poww;
		
		
		
		
		if numP >= 2**40/poww:
			result += "Case #%d: %d\n" %(caseNumber+1, i)
			return
			
		continue

		left = (1.0*P)/Q - frac;
		
		#if (left<0):
		#	continue

		NL = maxpow - maxpow/poww;
		#print i,NL
		
		BIG = NL*Q*poww;
		SMALL = (P*poww-Q)
		if (SMALL < 0):
			continue
		#if ((SMALL == 0) || (BIG % SMALL) == 0) {
		#if ((Q*poww) > (NL*(P*poww-Q))):
		#	continue
			
		if ((NL*(P*poww-Q)) % (Q*poww) == 0):
		
		#if ((abs((NL * left) - round((NL * left))) < 0.000001)):
			if caseNumber == 3:
				print i
				print NL
				print (P*poww-Q)
				print (NL*(P*poww-Q))
				print (Q*poww)
				print ((NL*(P*poww-Q)) % (Q*poww))
			result += "Case #%d: %d\n" %(caseNumber+1, i)
			return




		
	


	result += "Case #%d: impossible\n" %(caseNumber+1)
	return

	#result += "Case #%d: %d\n" %(caseNumber+1, kmin)
	
	
	
	"""if (('.' in A0) or ('.' in A1) or ('.' in A2) or ('.' in A3)):
		result += "Case #%d: %s\n" %(caseNumber, 'Game has not completed')
		return
	else:
		result += "Case #%d: %s\n" %(caseNumber, 'Draw')
		return
	
	"""
	



















file = open(INPUT_FILE, 'rb').read()

fileLines = file.split('\n')

T = int(fileLines[0])
nextLine = 1

result = ""

for caseNumber in xrange(T):

	R = fileLines[nextLine]
	
	r,t = [int(x) for x in R.split('/')]
	nextLine += 1
	
	SolveA(r,t)
	
	
#print result
open(OUTPUT_FILE, "wb").write(result)

