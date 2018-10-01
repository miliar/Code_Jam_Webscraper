import math
import cmath

def chunks(l, n):
    return (l[i:i+n] for i in xrange(0, len(l), n))

def winner(game, x , y):
	column = list()
	for row in game:
		column.append(row[y])

	# On a diagonal cell
	diag = list()
	rDiag = list()
	if(x == y):
		for i in range(4):
			diag.append(game[i][i])
			rDiag.append(game[3-i][i])

	row = game[y]
	rTotal = sum(row)
	cTotal = sum(column)
	dTotal = sum(diag)
	rdTotal = sum(rDiag)

	if(rTotal == 4 or cTotal == 4 or dTotal == 4 or rdTotal == 4):
		return 1
	elif (rTotal == -4 or cTotal == -4 or dTotal == -4 or rdTotal == -4):
		return -1
	if (rTotal == (3+1j) or cTotal == (3+1j) or dTotal == (3+1j) or rdTotal == (3+1j)):
		return 1
	elif (rTotal == (-3+1j) or cTotal == (-3+1j) or dTotal == (-3+1j) or rdTotal == (-3+1j)):
		return -1
	else:
		return 0

f = open('input.txt', 'r')

content = f.read();
lines = content.splitlines()
lines = lines[1:]
lines[:] = [x for x in lines if x != '']
for i, line in enumerate(lines):
	newList = list()
	for ch in line:
		if(ch == 'O'):
			newList.append(-1)
		elif(ch == 'X'):
			newList.append(1)
		elif(ch == '.'):
			newList.append(0)
		else:
			newList.append(complex(0, 1))
	lines[i] = newList

games = list(chunks(lines, 4))

i = 0
for game in games:
	blank = False
	i = i + 1
	wPlayer = 0

	for y, row in enumerate(game):
		for x, cell in enumerate(row):
			player = winner(game, x, y)
			if(player != 0):
				wPlayer = player
			# Full board test
			if(cell == 0):
				blank = True;

	if(wPlayer == 1):
		print("Case #"+str(i)+": X won")
	elif(wPlayer == -1):
		print("Case #"+str(i)+": O won")
	else:
		if(blank == False):
			# Game board is full with no winner
			print("Case #"+str(i)+": Draw")
		else:
			# Default case
			print("Case #"+str(i)+": Game has not completed")