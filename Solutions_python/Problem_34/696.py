
import re

inputText = open('input.txt', 'r').read()
	
def splitLines():
	return [token.strip() for token in inputText.split('\n')]
	
def getParams(firstLine):
	L, D, N = firstLine.split()			
	return int(L), int(D), int(N)

def getNextLine(splittedInput):
	return splittedInput.pop(0)

def getAllMatches(pattern, lexiconString):
	pattern = pattern.replace('(', '[')
	pattern = pattern.replace(')', ']')
	#print "pattern = ", pattern
	return re.findall(pattern, lexiconString)	

if __name__ == "__main__":
	
	splittedInput = splitLines()
	lexicon = []
	
	L, D, N = getParams(getNextLine(splittedInput))
	
	
	for x in range(D):
		lexicon.append(getNextLine(splittedInput))
	
	# we now have the lexicon, let's test the patterns
	curPattern = getNextLine(splittedInput)
	curTest = 1
	outFile = open('output.txt', 'w')
	
	while curPattern != '':
		outString = "Case #" + str(curTest) + ": " + str(len(getAllMatches(curPattern, ' '.join(lexicon) ) )) + "\n"
		print outString,
		outFile.write(outString)
		try :
			curPattern = getNextLine(splittedInput)
		except:
			curPattern = ''
		curTest += 1
	
	outFile.close()
	
