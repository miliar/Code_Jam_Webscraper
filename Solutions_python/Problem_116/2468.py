#!/bin/python

import os, sys

class Board:
	def __init__(self, strs):
		self.data = [[i for i in j] for j in strs]
		self.dat2 = [[row[k] for row in self.data] for k in range(len(self.data))]

	def _state(self):
		empty = False
		for board in [self.data, self.dat2]:	
			for row in board:
				if all([i == 'X' or i == 'T' for i in row]):
					return 0
				elif all([i == 'O' or i == 'T' for i in row]):
					return 1
				elif '.' in row:
					empty = True	
		diags = [[self.data[j][j] for j in range(4)], [self.data[j][3-j] for j in range(4)]]
		for temp in diags:
			if all([i == 'X' or i == 'T' for i in temp]):
				return 0
			if all([i == 'O' or i == 'T' for i in temp]):
				return 1
		return empty and 3 or 2

if __name__ == "__main__":
	outs = ["X won","O won", "Draw", "Game has not completed"]
	a = open(sys.argv[1]).read().split()
	ostr = []
	temp = 1
	ind = 0
	while ind < len(a):
		s = a[ind]
		if ind == 0:
			t = int(s)
			ind += 1
		elif s:
			ostr.append('Case #' + str(temp) + ': ' + outs[Board(a[ind:ind+4])._state()])
			temp += 1
			ind += 4
		else:
			ind += 1
	b = open('results.txt', 'wb')
	b.write('\n'.join(ostr))
	b.close()
		

			
	
