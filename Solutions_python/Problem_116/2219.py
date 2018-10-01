#! /bin/python

class Board:

	def __init__(self):
		self.b = [['.' for _ in range(4)] for _ in range(4)]
		self.complete = False

	def load(self, str_board):
		self.complete = True

		lines = str_board.split()
		for i in range(4):
			for j in range(4):
				self.b[i][j] = lines[i][j]
				if lines[i][j]=='.':
					self.complete=False

	def winner(self):
		d1=[]
		d2=[]
		for i in range(4):
			d1.append(self.b[i][i])
			d2.append(self.b[i][3-i])

		for player in ['X','O']:

			for i in range(4):

				if self.b[i].count(player)+self.b[i].count('T')==4:
					return player + " won"

				col=[]
				for c  in range(4):
					col.append(self.b[c][i])

				if col.count(player)+col.count('T')==4:
					return player + " won"

			if d1[:].count(player)+d1[:].count('T')==4 or d2[:].count(player)+d2[:].count('T')==4:
				return player + " won"

		if not self.complete:
			return "Game has not completed"
		else:
			return "Draw"



data=open("data", "r")
out=open("out", "w")

size = int(data.readline())
b = Board()
print size

for i in range(size):
	str_board=""

	for j in range(4):
		str_board += data.readline()

	data.readline() # \n entre les plateaux

	b.load(str_board)
	result=b.winner()

	out.write("Case #"+str(i+1)+": " + result+"\n")

data.close()
out.close()

