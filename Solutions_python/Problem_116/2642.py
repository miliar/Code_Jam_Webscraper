import os, sys, itertools

def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)


def checkBoard(b):
	empty_space_found = False
	for line in b:
		if '.' in line:
			empty_space_found = True
			continue
		if 'X' in line:
			if 'O' in line:
				continue
			else:
				return 'X'
		if 'O' in line:
			return 'O'
	if empty_space_found:
		return 'Game has not completed'
	return 'Draw'
				

fi = open('A-small-attempt0.in')
lines = fi.readlines()

for i,board in enumerate([[l[:-1] for l in line[:-1]] for line in grouper(5,lines[1:])]):
	winner = checkBoard(board)
	if winner in ['X','O']:
		print "Case #%s: %s won" % (i+1,winner)
		continue
	winner = checkBoard([''.join(item) for item in zip(*board)])
	if winner in ['X','O']:
		print "Case #%s: %s won" % (i+1,winner)
		continue
	diag1 = board[0][0]+board[1][1]+board[2][2]+board[3][3]
	diag2 = board[0][-1]+board[1][-2]+board[2][-3]+board[3][-4]
	winner = checkBoard([diag1,diag2])
	if winner in ['X','O']:
		print "Case #%s: %s won" % (i+1,winner)
		continue
	print "Case #%s: %s" % (i+1,winner)
	
	
