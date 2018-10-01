import psyco
psyco.full()

global known
global matches

def canBe(word):
	global known
	
	for other in known:
		if word in other:
			return True

def findAllWords(posWord, semiword, L, indice):
	global known
	global matches
	if indice == L-1:
		for i in range(len(posWord[indice])):
			if semiword + posWord[indice][i] in known:
				matches += 1
	else:
		for i in range(len(posWord[indice])):
			if canBe(semiword + posWord[indice][i]):
				findAllWords(posWord, semiword + posWord[indice][i], L, indice +1)

def getCombinations(L, known, word):
	global matches
	matches = 0
	posWord = []
	
	for i in range(L):
		posWord.append(0)
	
	currentPos = 0
	inParen = False
	for car in word:
		if inParen:
			if car == ')':
				inParen = False
				currentPos += 1
			else:
				posWord[currentPos].append(car)
		elif car == '(':
			inParen = True
			posWord[currentPos] = []
		else:
			posWord[currentPos] = [car]
			currentPos += 1
	
	findAllWords(posWord, '', L, 0)
	
	return matches
	
data = open('alien.txt', 'r').read().split('\n')

(L, D, N) = data.pop(0).split(' ')

L = int(L)
D = int(D)
N = int(N)

known = []
cases = []

for i in range(D):
	known.append(data.pop(0).strip())

for i in range(N):
	cases.append(data.pop(0).strip())

for case in range(len(cases)):
	print 'Case #' + str(case+1) + ': ' + str(getCombinations(L, known, cases[case]))
