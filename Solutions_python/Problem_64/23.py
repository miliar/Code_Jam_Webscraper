#!/usr/bin/env python3.1

import sys

def calc(rows, cols, data):
	board = convert_data(data)
	found = {}
	for size in reversed(range(1,1+min(rows, cols))):
		for r in range(rows-size+1):
			for c in range(cols-size+1):
				#print(board)
				if valid([board[r2][c:c+size] for r2 in range(r, r+size)]):
					if size not in found: found[size]=0
					found[size] += 1
					for r2 in range(r, r+size):
						board[r2][c:c+size] = [2]*size
	return format_result(found)

def valid(board):
	for r in range(len(board)):
		if 2 in board[r]: return False
		if r > 0 and board[r][0] == board[r-1][0]: return False
		for c in range(1, len(board[r])):
			if board[r][c] == board[r][c-1]: return False
	return True

def format_result(counts):
	c = sorted(counts.items())
	c.reverse()
	out = str(len(c))
	for size, count in c:
		out += '\n%d %d' % (size, count)
	return out

bin = {'0':[0,0,0,0],'1':[0,0,0,1],'2':[0,0,1,0],'3':[0,0,1,1],
       '4':[0,1,0,0],'5':[0,1,0,1],'6':[0,1,1,0],'7':[0,1,1,1],
       '8':[1,0,0,0],'9':[1,0,0,1],'A':[1,0,1,0],'B':[1,0,1,1],
       'C':[1,1,0,0],'D':[1,1,0,1], 'E':[1,1,1,0], 'F':[1,1,1,1]}
def convert_data(data):
	board = []
	for row in data:
		r = []
		for hex in row:
			r += bin[hex]
		board.append(r)
	return board

def getints():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

numTestCases = getints()[0]
for i in range(numTestCases):
	rows, cols = getints()
	data = [sys.stdin.readline().strip() for i in range(rows)]
	result = calc(rows, cols, data)
	print("Case #%d: %s" % (i+1, result))
