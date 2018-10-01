# -*- coding: utf-8 -*-
#
# Copyright 2013 Eric Shtivelberg
#


import sys

problem = 'A'

# Parse the input file
input_file_name = sys.argv[1]
assert input_file_name[-3:] == '.in', input_file_name

# Parse the output file
output_file_name = sys.argv[2] if len(sys.argv) > 2 else None
if output_file_name:
	assert output_file_name[-4:] == '.out', output_file_name
else:
	output_file_name = problem + '.out'

# Open the input file
input_file = open(input_file_name)

# The output list
output = []

lines = map(str.strip, input_file.readlines())
input_file.close()
def read_line(): return lines.pop(0)
def read_parts(): return lines.pop(0).split(' ')
def read_int(): return int(lines.pop(0))
def read_ints(): return map(int, lines.pop(0).split(' '))
def read_float(): return int(lines.pop(0))
def read_floats(): return map(float, lines.pop(0).split(' '))


########## Contest Specific ##########


T = read_int()
assert T >= 1, T

while lines:
	rows = [read_line() for i in xrange(4)]
	if lines: read_line()

	X_won = False
	O_won = False

	# print rows
	for i in xrange(4):
		# By row
		row = rows[i].replace('X', '')
		empty_num = row.count('.')
		if not row:
			X_won = True
			break
		elif len(row) == 4 and not empty_num:
			O_won = True
			break
		elif len(row) == 1 and row[0] == 'T':
			X_won = True
			break

		# By col
		col = ''.join([rows[y][i] for y in xrange(4)]).replace('X', '')
		# print 'col', col
		empty_num = col.count('.')

		if not col:
			X_won = True
			break
		elif len(col) == 4 and not empty_num:
			O_won = True
			break
		elif len(col) == 1 and col[0] == 'T':
			X_won = True
			break

	if not O_won and not X_won:
		diagonal1 = ''.join([rows[i][i] for i in xrange(4)]).replace('X', '')
		# print 'diagonal1', diagonal1
		empty_num = diagonal1.count('.')

		if not diagonal1:
			X_won = True
		elif len(diagonal1) == 4 and not empty_num:
			O_won = True
		elif len(diagonal1) == 1 and diagonal1[0] == 'T':
			X_won = True

	if not O_won and not X_won:
		diagonal2 = ''.join([rows[i][-i - 1] for i in xrange(4)]).replace('X', '')
		# print 'diagonal2', diagonal2
		empty_num = diagonal2.count('.')

		if not diagonal2:
			X_won = True
		elif len(diagonal2) == 4 and not empty_num:
			O_won = True
		elif len(diagonal2) == 1 and diagonal2[0] == 'T':
			X_won = True

	if X_won: output.append('X won')
	elif O_won: output.append('O won')
	else:
		has_dots = ''.join(rows).count('.')
		output.append('Draw' if not has_dots else 'Game has not completed')


########## Contest Specific End ##########


# print output
print "Closed input file..."

# Write the output
output_file = open(output_file_name, 'w')

cases = ['Case #{}: {}'.format(i+1, output[i]) for i in range(len(output))]
output_file.write('\n'.join(cases))

output_file.close()
print "Closed output file..."