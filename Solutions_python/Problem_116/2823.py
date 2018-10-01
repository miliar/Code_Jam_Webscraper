class Board:
	def __init__(self, inputFile):
		self.lines = []
		for i in range(0, 4):
			self.lines.append(inputFile.readline().strip())
		self.IsDraw = False
		self.Winner = None
		self.HasFreeCells = False
	
	def GetResult(self):
		self.GetLinesWinner()
		self.GetDiagonalWinner()
		self.RotateBoard()
		self.GetLinesWinner()
		self.GetDiagonalWinner()		
		if self.IsDraw:
			return 'Draw'
		elif self.Winner != None:
			return self.Winner + ' won'
		elif self.HasFreeCells:
			return 'Game has not completed'
		return 'Draw'

	def RotateBoard(self):
		newLines = []
		newLines.append('')
		newLines.append('')
		newLines.append('')
		newLines.append('')
		index = 0
		for line in self.lines:
			index = 0
			for letter in line:
				newLines[index] = newLines[index] + letter
				index = index + 1
			print str(newLines)
		self.lines = newLines
	
	def GetLineWinner(self, line):
		currentwinner = None
		for letter in line:
			if letter == '.':
				self.HasFreeCells = True
				return None
			elif currentwinner != None:
				if letter != 'T':
					if letter != currentwinner:
						return None
			elif currentwinner == None:
				currentwinner = letter
		if currentwinner != None:
			print 'winner for line ' + line + ' is ' + currentwinner
			if(self.Winner == None):
				self.Winner = currentwinner
			elif(self.Winner != currentwinner):
				self.IsDraw = True
		else:
			print 'no winner for line ' + line


	def GetDiagonalWinner(self):
		print self.lines
		diagonal = self.lines[0][0] + self.lines[1][1] + self.lines[2][2] + self.lines[3][3]
		self.GetLineWinner(diagonal)
		diagonal = self.lines[3][0] + self.lines[2][1] + self.lines[1][2] + self.lines[0][3]
		self.GetLineWinner(diagonal)


	def GetLinesWinner(self):
		for line in self.lines:
			winner = self.GetLineWinner(line)					
		

inputFile = open('A-small-attempt0.in', 'r')
outputFile = open('small.out', 'w')

T = int(inputFile.readline())

for i in range(1,T+1):
	board = Board(inputFile)
	inputFile.readline()
	outputFile.write('Case #' + str(i) + ': ' + board.GetResult() + '\n')
inputFile.close()
outputFile.close()