import os, inspect

problemName   = 'tidy_number'

def check(n):
	chaine = str(n)
	char = chaine[0]
	for c in chaine:
		if(int(c) < int(char)):
			return False
		char = c
	return True

def solution(n):
	if(check(n)):
		return n
	else:
		for i in range(n):
			if(check(n - i)):
				return n - i

currentDir   = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
inputString  = 'B-small-attempt0.in'
outputString = problemName + '_output'
inFile       = os.path.join(currentDir, inputString)
outFile      = os.path.join(currentDir, 'outputfiles', '%s.txt' % outputString)

if os.path.exists(outFile):
  os.remove(outFile)

with open(inFile, 'r') as inputfile:
  numberOfCases = int(inputfile.readline())
  for case in range(1, numberOfCases + 1):

    N = int(inputfile.readline())
    # Get the result here
    result = solution(N)

    with open(outFile, 'a') as f:
      f.write('Case #%d: %s\n' % (case, str(result)))