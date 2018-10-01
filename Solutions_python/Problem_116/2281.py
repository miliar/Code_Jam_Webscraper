#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, os

#	print l

def isWhich(l):
	X = 'X won'
	O = 'O won'
	if l.count('.'): return False
	if l.count('T') == 1:
		if l.count('X') == 3: return X
		elif l.count('O') == 3: return O
	elif l.count('X') == 4: return X
	elif l.count('O') == 4: return O
	return False

def solve(sq):
#	print "-----------------------"
#	for i in sq:
#		print ''.join(i)
#	print "-----------------------"
#diagonal
	res = isWhich([sq[i][i] for i in range(4)])
	if res: return res
	res = isWhich([sq[y][x] for y,x in enumerate(reversed(range(4)))])
	if res: return res
#raw
	for raw in sq:
		res = isWhich(''.join(raw))
		if res: return res
#column
	for x in range(4):
		col = ""
		for y in range(4):
			col += sq[y][x]
		res = isWhich(col)
		if res: return res
	for i in sq:
		if i.count('.'): return "Game has not completed"
	else:
		return "Draw"
	
def main():
	n = int(sys.stdin.readline())
	for i in range(n):
		inp = []
		for l in range(4):
			row = sys.stdin.readline()
			if not row.strip():
				row = sys.stdin.readline()
			inp.append([p for p in row.strip()])
		res = solve(inp)
		print "Case #%d: %s"%(i+1, res)
	

if __name__ == '__main__':
	sys.exit(main())


