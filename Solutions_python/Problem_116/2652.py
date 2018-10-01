XWIN = (1, 'X won')
OWIN = (2, 'O won')
DRAW = (3, 'Draw')
NFIN = (4, 'Game has not completed')

def searchH(jogo):
	hasBlank = False
	
	for line in jogo:
		x, o = 0, 0
	
		for col in line:
			if col == '.':
				hasBlank = True
				break
			elif col == 'T':
				x+=1
				o+=1
			elif col == 'X': 
				x+=1
			elif col == 'O': 
				o+=1
			
		if x == 4: return 1
		if o == 4: return 2
	
	if hasBlank == False: 
		return 3
	else: 
		return 4

def searchX(jogo):
	newJogo = [
				[jogo[0][0], jogo[1][1], jogo[2][2], jogo[3][3]],
				[jogo[0][3], jogo[1][2], jogo[2][1], jogo[3][0]]
			]
	return searchH(newJogo)

def searchV(jogo):
	# Inverts the game layout, so can use searchH as well
	inverted = [map(lambda line: line[col], jogo) for col in xrange(0, 4)]
	return searchH(inverted)

def checkStatus(jogo):
	results = (searchH(jogo), searchV(jogo), searchX(jogo))

	if 1 in results:   return XWIN
	elif 2 in results: return OWIN
	elif 4 in results: return NFIN
	else:              return DRAW

def loadJogos(path):
	with open(path, "r") as f:
		lines = f.readlines()

	jogos = []
	jogo  = []
	for line in lines[1:]:

		if line != "\n":
			jogo.append(line.replace('\n', ''))
		else:
			jogos.append(jogo)
			jogo = []
		
	jogos.append(jogo)
	
	return jogos


if __name__ == "__main__":
	jogos = loadJogos("A-large.in")
	
	f = open("results.txt", "w")
	
	try:
		for n, jogo in enumerate(jogos, 1):
			result = checkStatus(jogo)
			res = "Case #%s: %s\n" % (n, result[1])
			print res
			f.write(res)
	except:
		pass
	
	f.close()			