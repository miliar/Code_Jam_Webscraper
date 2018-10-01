import sys

from math import log, floor, ceil
from itertools import takewhile, imap, count

def is_winning(lines, char):
	return any([all(map(lambda c: c == char or c == "T", line)) for line in lines])

def has_row(board, char):
	return is_winning(board, char)

def has_col(board, char):
	cols = [[line[j] for line in board] for j in range(4)]
	return is_winning(cols, char)

def has_diagonal(board, char):
	diag1 = [board[i][i] for i in range(4)]
	diag2 = [board[i][3 - i] for i in range(4)]
	return is_winning((diag1, diag2), char)

def won(board, char):
	return has_row(board, char) or has_col(board, char) or has_diagonal(board, char)

def free_space(board):
	return any(map(lambda line: "." in line, board))

def parse_case(inp):
	board = [inp.readline().strip() for _ in range(4)]
	
	expected_empty_line = inp.readline().strip()
	assert expected_empty_line == "", "Unexp.: %s" % expected_empty_line

	if won(board, "X"):
		return "X won"
	elif won(board, "O"):
		return "O won"
	elif free_space(board):
		return "Game has not completed"
	else:
		return "Draw"

def parse(fileName):
	results = []
	with open(fileName) as f:
		cases = int(f.readline())
		for i in range(cases):
			results.append(parse_case(f))

		next_line = f.readline()
		assert "" == next_line, "Unexpected line: %s" % next_line
	return results

if __name__ == "__main__":
	for (i, result) in enumerate(parse(sys.argv[1])):
		print "Case #%d: %s" % (i + 1, result)
