class Board:
	def __init__(self):
		self.rows = []
		self.hasemptyfield = False

	def addRow(self, line):
		if '.' in line: self.hasemptyfield = True
		self.rows.append(list(line.strip()))

	def getRow(self, index):
		return self.rows[index]

	def hasEmptyField(self):
		return self.hasemptyfield

	def solve(self):
		#first check the diagonals
		diagonal1 = True
		diagonal2 = True

		top_left = self.rows[0][0]
		top_right = self.rows[0][3]

		for i in range(1, 4):
			if self.rows[i][i] != top_left and self.rows[i][i] != 'T': diagonal1 = False
		for i in range(1, 4):
			if self.rows[i][3-i] != top_right and self.rows[i][3-i] != 'T': diagonal2 = False

		if (diagonal1 == True) and (top_left == 'X'): return 'X won'
		if (diagonal1 == True) and (top_left == 'O'): return 'O won'
		if (diagonal2 == True) and (top_right == 'X'): return 'X won'
		if (diagonal2 == True) and (top_right == 'O'): return 'O won'

		#then check rows and columns
		X_rows = []
		O_rows = []
		
		for i in range(0, 4):
			X_rows_num = 0
			O_rows_num = 0
			X_cols_num = 0
			O_cols_num = 0
			for j in range(0, 4):
				#check rows
				if self.rows[i][j] == 'X' or self.rows[i][j] == 'T': X_rows_num += 1
				if self.rows[i][j] == 'O' or self.rows[i][j] == 'T': O_rows_num += 1
				#check columns
				if self.rows[j][i] == 'X' or self.rows[j][i] == 'T': X_cols_num += 1
				if self.rows[j][i] == 'O' or self.rows[j][i] == 'T': O_cols_num += 1
			if X_rows_num == 4 or X_cols_num == 4 : return 'X won'
			if O_rows_num == 4 or O_cols_num == 4 : return 'O won'
		
		return False

	def clear(self):
		self.rows = []
		self.hasemptyfield = False
	def getLength(self):
		return len(self.rows)
	
f = open('A-small-attempt0.in')
output = open('output_A.txt', 'w')

def echo(line):
	print line
	output.write(line + '\n')

n = 0
board = Board()
cases = int(f.readline())

for line in f:
	if line != '\n':
		board.addRow(line)
	if board.getLength() == 4:
		n += 1
		result = board.solve()
		if result == False:
			if board.hasEmptyField() == True:
				echo('Case #' + str(n) + ': Game has not completed')
			else:
				echo('Case #' + str(n) + ': Draw')
		else:
			echo('Case #' + str(n) + ': ' + result)
		board.clear()

f.close()
output.close()
