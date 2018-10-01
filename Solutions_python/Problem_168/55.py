#!/usr/bin/python

import sys, Queue

def testUp(board, h, w, i, j):
	while i - 1 >= 0:
		i -= 1
		if board[i][j] != '.':
			return True
	return False

def testDown(board, h, w, i, j):
	while i + 1 < h:
		i += 1
		if board[i][j] != '.':
			return True
	return False

def testLeft(board, h, w, i, j):
	while j - 1 >= 0:
		j -= 1
		if board[i][j] != '.':
			return True
	return False

def testRight(board, h, w, i, j):
	while j + 1 < w:
		j += 1
		if board[i][j] != '.':
			return True
	return False

def examineCell(board, h, w, i, j):
	c = board[i][j]
	if c == '<' and testLeft(board, h, w, i, j):
		return 0
	if c == '>' and testRight(board, h, w, i, j):
		return 0
	if c == '^' and testUp(board, h, w, i, j):
		return 0
	if c == 'v' and testDown(board, h, w, i, j):
		return 0

	valid = 0
	if testUp(board, h, w, i, j):
		valid += 1
	if testDown(board, h, w, i, j):
		valid += 1
	if testLeft(board, h, w, i, j):
		valid += 1
	if testRight(board, h, w, i, j):
		valid += 1

	if c == '.':
		return 0
	
	if valid > 0:
		return 1
	
	return -1

def examineBoard(board, h, w):
	count = 0
	for i in range(h):
		for j in range(w):
			val = examineCell(board, h, w, i, j)

			if val == -1:
				return "IMPOSSIBLE"
			else:
				count += val

	return count

if __name__ == "__main__":
	lines = int(sys.stdin.readline())
	for i in range(lines):
		h,w = map(int, sys.stdin.readline().split())
		board = []
		for j in range(h):
			s = sys.stdin.readline().strip()
			board.append(s)

		print("Case #{0}: {1}".format(str(i+1), examineBoard(board, h, w)))
