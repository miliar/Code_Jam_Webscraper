import sys, math

def nInsertionsToNextMote(mote, A):
	nInsertions = int(math.ceil(math.log((mote - A)/((A - 1)) + 1,2)))
	A += (2**(nInsertions) - 1)*(A - 1)
	return nInsertions, A

def moteEating(motes, A, nOperations, minimum):
	if len(motes) != 0:
		if A > motes[0]:
			A += motes.pop(0)
		else:
			if A + A - 1 > motes[0]: #one insertion solves
				A += A - 1
				nOperations += 1
			else:
				if A > 1:
					nInsertions, newA = nInsertionsToNextMote(motes[0], A)
					if nOperations + nInsertions > minimum:
						nOperationsNInsertions = 1e7
					else:
						nOperationsNInsertions = moteEating(motes[:], newA, nOperations + nInsertions, minimum)
				else:
					nOperationsNInsertions = 1e7
				motesRemoval = motes[:]
				motesRemoval.pop(0)
				nOperationsRemoval = moteEating(motesRemoval, A, nOperations + 1, minimum)
				
				return min([nOperationsRemoval, nOperationsNInsertions])
		nOperations = moteEating(motes, A, nOperations, minimum)
		
	return nOperations

inputFileName = sys.argv[1]

f = file(inputFileName)
fout = file("outputA.txt", "w")

T = eval(f.readline())

for i in xrange(T):
	A, N = f.readline().strip().split()
	A = eval(A)
	N = eval(N)
	
	motes = f.readline().strip().split()
	for j in xrange(N):
		motes[j] = eval(motes[j])
	
	motes.sort()
	
	nOperations = moteEating(motes, A, 0, N)
				
	# Output writing
	fout.write("Case #%d: %d\n" %(i + 1, nOperations))
