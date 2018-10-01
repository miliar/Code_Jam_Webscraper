########### Load input
f = open('A-large.in', 'r')
lines = f.readlines()
nb = int(lines[0])
f.closed
string = ''
i = 1
no = 1
while i <= len(lines)-4:
	table= [ [ '?' for i in range(4) ] for j in range(4) ]
	nf = 0
	for x in range(4):
		table[x] = lines[i+x]	
		if lines[i+x].find('.') != -1:
			nf = 1	
	wX, wO = 0, 0
	
	for x in range(4):
		nO, nX = 0, 0 
		for y in range(4):
			if table[x][y] == 'X':
				nX += 1
			if table[x][y] == 'O':
				nO += 1	
			if table[x][y] == 'T':
				nO += 1
				nX += 1
		if nX == 4:
			wX += 1
		if nO == 4:
			wO += 1
		
	for x in range(4):
		nO, nX = 0, 0 
		for y in range(4):
			if table[y][x] == 'X':
				nX += 1
			if table[y][x] == 'O':
				nO += 1	
			if table[y][x] == 'T':
				nO += 1
				nX += 1
		if nX == 4:
			wX += 1
		if nO == 4:
			wO += 1

	nO, nX = 0, 0 
	for x in range(4):
		if table[x][x] == 'X':
			nX += 1
		if table[x][x] == 'O':
			nO += 1	
		if table[x][x] == 'T':
			nO += 1
			nX += 1
	if nX == 4:
		wX += 1
	if nO == 4:
		wO += 1	
		
	nO, nX = 0, 0 		
	for x in range(4):
		if table[x][3-x] == 'X':
			nX += 1
		if table[x][3-x] == 'O':
			nO += 1	
		if table[x][3-x] == 'T':
			nO += 1
			nX += 1		
	if nX == 4:
		wX += 1
	if nO == 4:
		wO += 1
		
	string += 'Case #{0}: '.format(no)
	no += 1
	if wX > 0 and wO == 0:
		text = 'X won'
	if wO > 0 and wX == 0:
		text = 'O won'
	if wX > 0 and wO > 0:
		text = 'Draw'
	if (wX == 0 and wO == 0) and (nf == 0):
		text = 'Draw'			
	if (wX == 0 and wO == 0) and (nf == 1):
		text = 'Game has not completed'	
			
	string += '{0}\n' .format(text)
	
	i = i + 5				

########### Write output
f = open('A-large.out', 'w')	
f.write(string)
f.closed
		