#!/usr/bin/env pypy
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2011–2013 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

from common import nt, ni, nl, line


"""
Tic-TAc-Toe-Tomek
"""

def four(*args):
	T = args.count("T")
	for P in "XO":
		if args.count(P) + T == 4:
			return P
	return None

def lines(board):
	for line in board:
		yield line
def columns(board):
	for line in zip(*board):
		yield line
def diagonals(board):
	yield [board[i][i] for i in range(4)]
	yield [board[i][3-i] for i in range(4)]
		
def status(board):
	not_completed = False
	for quadruplets in [lines, columns, diagonals]:
		for quadruplet in quadruplets(board):
			not_completed |= "." in quadruplet
			P = four(*quadruplet)
			if P:
				return "%s won" % P
	
	if not_completed:
		return "Game has not completed"
	else:
		return "Draw"


T = ni();
for X in xrange(T):
	nl()
 	print "Case #%s:" % (X+1),
	board = [list(*line()), list(*line()), list(*line()), list(*line())]
	print status(board)
