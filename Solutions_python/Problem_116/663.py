import os
import sys

entries = int(sys.stdin.readline())

case = 1
for case in range(1, entries + 1):
	grid = [tuple(sys.stdin.readline().strip()) for x in range(4)]

	sys.stdin.readline() # Clear the empty line

	def check_horiz(grid):
		for row in grid:
			won = None
			if row.count('T') + row.count('O') == 4:
				won = 'O'
			elif row.count('T') + row.count('X') == 4:
				won = 'X'
			if won:
				print "Case #%s: %s won" % (case, won)
				return True
		return False

	if check_horiz(grid):
		continue
	elif check_horiz(zip(*grid)):
		continue

	elif check_horiz([[grid[x][x] for x in range(4)], [grid[3-x][x] for x in range(4)]]):
		continue

	if any(('.' in x for x in grid)):
		print "Case #%s: Game has not completed" % (case)
		continue
	else:
		print "Case #%s: Draw" % (case)

