#!/usr/bin/python

import sys

def check_line(line):
	lineX = line.replace('T', 'X')
	lineO = line.replace('T', 'O')
	if lineX == 'XXXX':
		return 1
	elif lineO == 'OOOO':
		return 2
	elif line.find('.') > -1:
		# not finished
		return 3
	else:
		# draw
		return 4
	

def reverse_lines(lines):
	new_lines = []
	for i in range(0, 4):
		new_lines.append([])
		for j in range(0, 4):
			new_lines[i].append(lines[j][i])
		new_lines[i] = ''.join(new_lines[i])
	#print lines
	#print new_lines
	return new_lines

def make_diagonals(lines):
	diagonals = []
	diagonals.append([])
	diagonals.append([])
	#print lines
	for i in range(0, 4):
		diagonals[0].append(lines[i][i])
	diagonals[0] = ''.join(diagonals[0])
	
	for i in range(0, 4):
		diagonals[1].append(lines[i][3 - i])
	diagonals[1] = ''.join(diagonals[1])
	return diagonals

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

ntests = int(fin.readline().rstrip())
#print ntests

for i in range(0, ntests):
	#print i
	lines = []
	result = ''
	ostatus = 0
	vstatus = 0
	dstatus = 0
	finished = True
	draw = False
	# read and check horizontal lines
	for j in range(0,4):
		lines.append(fin.readline().rstrip())
	for j in range(0,4):
		ostatus = check_line(lines[j])
		if ostatus == 1:
			result = 'X won'	
			break
		elif ostatus == 2:
			result = 'O won'
			break
		elif ostatus == 3:
			finished = False
		elif ostatus == 4:
			draw = True
	# check the verticals
	if ostatus not in ( 1, 2):
		verticals = reverse_lines(lines)
		for j in range(0, 4):
			vstatus = check_line(verticals[j])
			if vstatus == 1:
				result = 'X won'
				break
			elif vstatus == 2:
				result = 'O won'
				break
			elif vstatus == 3:
				finished = False
			else:
				draw = True

		# check diagonals
		if vstatus not in (1, 2):
			diagonals = make_diagonals(lines)
			for j in range(0, 2):
				dstatus = check_line(diagonals[j])
				if dstatus == 1:
					result = 'X won'
					break
				elif dstatus == 2:
					result = 'O won'
					break
				elif dstatus == 3:
					finished = False
				else:
					draw = True

			if dstatus not in (1, 2):
				if not finished:
					result = 'Game has not completed'
				else:
					result = 'Draw'
	
	fout.write("Case #" + str(i+1) + ": " + result + "\n")
	if i < (ntests -1):
		fin.readline()

fin.close()
fout.close()


