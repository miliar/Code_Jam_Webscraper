#!  /usr/bin/env python
import sys

rl = sys.stdin.readline

cases = int(rl().strip())

lines = []

num_dot = 0

def check_rows():
	global lines
	global num_dot
	for l in lines:
		num_x = 0
		num_o = 0
		num_t = 0
		for c in l:
			if c == 'X':
				num_x = num_x + 1
			elif c == 'O':
				num_o = num_o + 1
			elif c == 'T':
				num_t = num_t + 1
			elif c == '.':
				num_dot = num_dot + 1
		if num_t == 1:
			if num_x == 3:
				return 'X won'
			elif num_o == 3:
				return 'O won'
		else:
			if num_x == 4:
				return 'X won'
			elif num_o == 4:
				return 'O won'
	return None

def check_cols():
	global lines
	global num_dot
	for i in range(4):
		num_x = 0
		num_o = 0
		num_t = 0
		for j in range(4):
			if lines[j][i] == 'X':
				num_x = num_x + 1
			elif lines[j][i] == 'O':
				num_o = num_o + 1
			elif lines[j][i] == 'T':
				num_t = num_t + 1
			elif lines[j][i] == '.':
				num_dot = num_dot + 1
		if num_t == 1:
			if num_x == 3:
				return 'X won'
			elif num_o == 3:
				return 'O won'
		else:
			if num_x == 4:
				return 'X won'
			elif num_o == 4:
				return 'O won'
	return None

def check_diag():
	global lines
	global num_dot
	num_x = 0
	num_o = 0
	num_t = 0
	for i in range(4):
		if lines[i][i] == 'X':
			num_x = num_x + 1
		elif lines[i][i] == 'O':
			num_o = num_o + 1
		elif lines[i][i] == 'T':
			num_t = num_t + 1
		elif lines[i][i] == '.':
			num_dot = num_dot + 1
	if num_t == 1:
		if num_x == 3:
			return 'X won'
		elif num_o == 3:
			return 'O won'
	else:
		if num_x == 4:
			return 'X won'
		elif num_o == 4:
			return 'O won'

	num_x = 0
	num_o = 0
	num_t = 0
	for i in range(4):
		if lines[i][3-i] == 'X':
			num_x = num_x + 1
		elif lines[i][3-i] == 'O':
			num_o = num_o + 1
		elif lines[i][3-i] == 'T':
			num_t = num_t + 1
		elif lines[i][3-i] == '.':
			num_dot = num_dot + 1
	if num_t == 1:
		if num_x == 3:
			return 'X won'
		elif num_o == 3:
			return 'O won'
	else:
		if num_x == 4:
			return 'X won'
		elif num_o == 4:
			return 'O won'
	return None

for c in range(1, cases+1):
	num_dot = 0
	lines = []
	for i in range(4):
		lines.append( rl().strip() )
	rl()

	res = check_rows()
	if res != None:
		print "Case #%d: %s" % ( c, res )
		continue
	res = check_cols()
	if res != None:
		print "Case #%d: %s" % ( c, res )
		continue
	res = check_diag()
	if res != None:
		print "Case #%d: %s" % ( c, res )
		continue
	if num_dot == 0:
		print "Case #%d: Draw" % ( c )
	else:
		print "Case #%d: Game has not completed" % ( c )
