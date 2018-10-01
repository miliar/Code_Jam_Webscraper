myFile = open('codeJam.txt');
lines = myFile.readlines();
myFile.close();

numberOfGames = int(lines[0]);

winner = 0;
noWinner = 'Draw';
notOver = 'Game has not completed';

def printLines():
	for i in range(numberOfGames):
		for j in range(5):
			print lines[1+i*5+j];
	
 
def printGame(game):
	for i in range(4):
		line = lines[1+game*5 + i];
		print line;

def checkWinnerWithCounts(xCount, oCount, tCount, dotCount):
	if xCount == 4:
		return 'X won';
	if xCount == 3:
		if tCount == 1:
			return 'X won';
	if oCount == 4:
		return 'O won';
	if oCount == 3:
		if tCount == 1:
			return 'O won';

	if dotCount > 0:
		return notOver;
	
	return noWinner;
	
def checkLine(line):
	x = 0;
	o = 0;
	t = 0;
	dot = 0;
	for letter in line:
		if letter == 'X':
			x+=1;
		if letter == 'O':
			o+=1;
		if letter == 'T':
			t+=1;
		if letter == '.':
			dot+=1;
	return checkWinnerWithCounts(x,o,t,dot);

	
def valueFor(gameNumber, col, row):
	line = lines[1+gameNumber*5+row];
	return line[col];



def checkRow(gameNumber, rowNumber):
	a = valueFor(gameNumber, 0, rowNumber);
	b = valueFor(gameNumber, 1, rowNumber);
	c = valueFor(gameNumber, 2, rowNumber);
	d = valueFor(gameNumber, 3, rowNumber);
	line = a + b + c + d;
	return checkLine(line);	


def checkCol(gameNumber, colNumber):
	a = valueFor(gameNumber, colNumber, 0);
	b = valueFor(gameNumber, colNumber, 1);
	c = valueFor(gameNumber, colNumber, 2);
	d = valueFor(gameNumber, colNumber, 3);
	line = a + b + c + d;
	return checkLine(line);


def checkDiagonals(gameNumber):
	gameRunning = False;
	a = valueFor(gameNumber, 0, 0);
	b = valueFor(gameNumber, 1, 1);
	c = valueFor(gameNumber, 2, 2);
	d = valueFor(gameNumber, 3, 3);
	line = a + b + c + d;
	tmp = checkLine(line);

	if tmp != noWinner:
		if tmp == notOver:
			gameRunning = True;
		else:
			return tmp;

	a = valueFor(gameNumber, 3, 0);
	b = valueFor(gameNumber, 2, 1);
	c = valueFor(gameNumber, 1, 2);
	d = valueFor(gameNumber, 0, 3);
	line = a + b + c + d;
	tmp = checkLine(line);
	if tmp != noWinner:
		if tmp == notOver:
			gameRunning = True;
		else:
			return tmp;

	if gameRunning:
		return notOver;

	return noWinner;







def checkGame(game):
	gameRunning = False;
	if game >= numberOfGames:
		return 'outside bounds';

	for r in range(4):
		tmp = checkRow(game, r);
		if tmp != noWinner:
			if tmp == notOver:
				gameRunning = True;
			else:
				return tmp;
	for c in range(4):
		tmp = checkCol(game, c);
		if tmp != noWinner:
			if tmp == notOver:
				gameRunning = True;
			else:
				return tmp;

	tmp = checkDiagonals(game);
	if tmp != noWinner:
		if tmp == notOver:
			gameRunning = True;
		else:
			return tmp;

	if gameRunning:
		return notOver;

	return noWinner;

for i in range(numberOfGames):
	print 'Case #' + str(i+1) + ': ' + checkGame(i);