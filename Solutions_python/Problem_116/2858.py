import sys

numGames = int(raw_input())
for game in range(1, numGames+1):
	grid = []
	for row in range(0,4):
		line = raw_input()
		grid.append(list(line))
	incomplete = 0
	solved = 0
	rowEmpty = [0,0,0,0]
	colEmpty = [0,0,0,0]

	if grid[0][0] == '.':
		incomplete = 1
		rowEmpty[0] = 1
		colEmpty[0] = 1
	elif grid[0][0] == 'X':
		if grid[1][1] == '.':
			incomplete = 1
			rowEmpty[1] = 1
			colEmpty[1] = 1
		elif grid[1][1] == 'X' or grid[1][1] == 'T':
			if grid[2][2] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[2] = 1
			elif grid[2][2] == 'X' or grid[2][2] == 'T':
				if grid[3][3] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[3] = 1
				elif grid[3][3] == 'X' or grid[3][3] == 'T':
					solved = 1
					print "Case #%d: X won" % (game)
	elif grid[0][0] == 'O':
		if grid[1][1] == '.':
			incomplete = 1
			rowEmpty[1] = 1
			colEmpty[1] = 1
		elif grid[1][1] == 'O' or grid[1][1] == 'T':
			if grid[2][2] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[2] = 1
			elif grid[2][2] == 'O' or grid[2][2] == 'T':
				if grid[3][3] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[3] = 1
				elif grid[3][3] == 'O' or grid[3][3] == 'T':
					solved = 1
					print "Case #%d: O won" % (game)
	elif grid[0][0] == 'T':
		if grid[1][1] == '.':
			incomplete = 1
			rowEmpty[1] = 1
			colEmpty[1] = 1
		elif grid[1][1] == 'X':
			if grid[2][2] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[2] = 1
			elif grid[2][2] == 'X':
				if grid[3][3] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[3] = 1
				elif grid[3][3] == 'X':
					solved = 1
					print "Case #%d: X won" % (game)
		elif grid[1][1] == 'O':
			if grid[2][2] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[2] = 1
			elif grid[2][2] == 'O':
				if grid[3][3] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[3] = 1
				elif grid[3][3] == 'O':
					solved = 1
					print "Case #%d: O won" % (game)

	if not solved:
		if grid[3][0] == '.':
			incomplete = 1
			rowEmpty[3] = 1
			colEmpty[0] = 1
		elif grid[3][0] == 'X':
			if grid[2][1] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[1] = 1
			elif grid[2][1] == 'X' or grid[2][1] == 'T':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'X' or grid[1][2] == 'T':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'X' or grid[0][3] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[3][0] == 'O':
			if grid[2][1] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[1] = 1
			elif grid[2][1] == 'O' or grid[2][1] == 'T':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'O' or grid[1][2] == 'T':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'O' or grid[0][3] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[3][0] == 'T':
			if grid[2][1] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[1] = 1
			elif grid[2][1] == 'X':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'X':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[2][1] == 'O':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'O':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not rowEmpty[0]:
		if grid[0][0] == '.':
			incomplete = 1
			rowEmpty[0] = 1
			colEmpty[0] = 1
		elif grid[0][0] == 'X':
			if grid[0][1] == '.':
				incomplete = 1
				rowEmpty[0] = 1
				colEmpty[1] = 1
			elif grid[0][1] == 'X' or grid[0][1] == 'T':
				if grid[0][2] == '.':
					incomplete = 1
					rowEmpty[0] = 1
					colEmpty[2] = 1
				elif grid[0][2] == 'X' or grid[0][2] == 'T':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'X' or grid[0][3] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[0][0] == 'O':
			if grid[0][1] == '.':
				incomplete = 1
				rowEmpty[0] = 1
				colEmpty[1] = 1
			elif grid[0][1] == 'O' or grid[0][1] == 'T':
				if grid[0][2] == '.':
					incomplete = 1
					rowEmpty[0] = 1
					colEmpty[2] = 1
				elif grid[0][2] == 'O' or grid[0][2] == 'T':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'O' or grid[0][3] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[0][0] == 'T':
			if grid[0][1] == '.':
				incomplete = 1
				rowEmpty[0] = 1
				colEmpty[1] = 1
			elif grid[0][1] == 'X':
				if grid[0][2] == '.':
					incomplete = 1
					rowEmpty[0] = 1
					colEmpty[2] = 1
				elif grid[0][2] == 'X':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[0][1] == 'O':
				if grid[0][2] == '.':
					incomplete = 1
					rowEmpty[0] = 1
					colEmpty[2] = 1
				elif grid[0][2] == 'O':
					if grid[0][3] == '.':
						incomplete = 1
						rowEmpty[0] = 1
						colEmpty[3] = 1
					elif grid[0][3] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not rowEmpty[1]:
		if grid[1][0] == '.':
			incomplete = 1
			rowEmpty[1] = 1
			colEmpty[0] = 1
		elif grid[1][0] == 'X':
			if grid[1][1] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[1] = 1
			elif grid[1][1] == 'X' or grid[1][1] == 'T':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'X' or grid[1][2] == 'T':
					if grid[1][3] == '.':
						incomplete = 1
						rowEmpty[1] = 1
						colEmpty[3] = 1
					elif grid[1][3] == 'X' or grid[1][3] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[1][0] == 'O':
			if grid[1][1] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[1] = 1
			elif grid[1][1] == 'O' or grid[1][1] == 'T':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'O' or grid[1][2] == 'T':
					if grid[1][3] == '.':
						incomplete = 1
						rowEmpty[1] = 1
						colEmpty[3] = 1
					elif grid[1][3] == 'O' or grid[1][3] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[1][0] == 'T':
			if grid[1][1] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[1] = 1
			elif grid[1][1] == 'X':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'X':
					if grid[1][3] == '.':
						incomplete = 1
						rowEmpty[1] = 1
						colEmpty[3] = 1
					elif grid[1][3] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[1][1] == 'O':
				if grid[1][2] == '.':
					incomplete = 1
					rowEmpty[1] = 1
					colEmpty[2] = 1
				elif grid[1][2] == 'O':
					if grid[1][3] == '.':
						incomplete = 1
						rowEmpty[1] = 1
						colEmpty[3] = 1
					elif grid[1][3] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not rowEmpty[2]:
		if grid[2][0] == '.':
			incomplete = 1
			rowEmpty[2] = 1
			colEmpty[0] = 1
		elif grid[2][0] == 'X':
			if grid[2][1] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[1] = 1
			elif grid[2][1] == 'X' or grid[2][1] == 'T':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'X' or grid[2][2] == 'T':
					if grid[2][3] == '.':
						incomplete = 1
						rowEmpty[2] = 1
						colEmpty[3] = 1
					elif grid[2][3] == 'X' or grid[2][3] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[2][0] == 'O':
			if grid[2][1] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[1] = 1
			elif grid[2][1] == 'O' or grid[2][1] == 'T':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'O' or grid[2][2] == 'T':
					if grid[2][3] == '.':
						incomplete = 1
						rowEmpty[2] = 1
						colEmpty[3] = 1
					elif grid[2][3] == 'O' or grid[2][3] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[2][0] == 'T':
			if grid[2][1] == '.':
				incomplete = 1
				rowEmpty[2] = 1
				colEmpty[1] = 1
			elif grid[2][1] == 'X':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'X':
					if grid[2][3] == '.':
						incomplete = 1
						rowEmpty[2] = 1
						colEmpty[3] = 1
					elif grid[2][3] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[2][1] == 'O':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'O':
					if grid[2][3] == '.':
						incomplete = 1
						rowEmpty[2] = 1
						colEmpty[3] = 1
					elif grid[2][3] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not rowEmpty[3]:
		if grid[3][0] == '.':
			incomplete = 1
			rowEmpty[3] = 1
			colEmpty[0] = 1
		elif grid[3][0] == 'X':
			if grid[3][1] == '.':
				incomplete = 1
				rowEmpty[3] = 1
				colEmpty[1] = 1
			elif grid[3][1] == 'X' or grid[3][1] == 'T':
				if grid[3][2] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[2] = 1
				elif grid[3][2] == 'X' or grid[3][2] == 'T':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'X' or grid[3][3] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[3][0] == 'O':
			if grid[3][1] == '.':
				incomplete = 1
				rowEmpty[3] = 1
				colEmpty[1] = 1
			elif grid[3][1] == 'O' or grid[3][1] == 'T':
				if grid[3][2] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[2] = 1
				elif grid[3][2] == 'O' or grid[3][2] == 'T':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'O' or grid[3][3] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[3][0] == 'T':
			if grid[3][1] == '.':
				incomplete = 1
				rowEmpty[3] = 1
				colEmpty[1] = 1
			elif grid[3][1] == 'X':
				if grid[3][2] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[2] = 1
				elif grid[3][2] == 'X':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[3][1] == 'O':
				if grid[3][2] == '.':
					incomplete = 1
					rowEmpty[3] = 1
					colEmpty[2] = 1
				elif grid[3][2] == 'O':
					if grid[1][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not colEmpty[0]:
		if grid[0][0] == '.':
			incomplete = 1
			rowEmpty[0] = 1
			colEmpty[0] = 1
		elif grid[0][0] == 'X':
			if grid[1][0] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[0] = 1
			elif grid[1][0] == 'X' or grid[1][0] == 'T':
				if grid[2][0] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[0] = 1
				elif grid[2][0] == 'X' or grid[2][0] == 'T':
					if grid[3][0] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[0] = 1
					elif grid[3][0] == 'X' or grid[3][0] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[0][0] == 'O':
			if grid[1][0] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[0] = 1
			elif grid[1][0] == 'O' or grid[1][0] == 'T':
				if grid[2][0] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[0] = 1
				elif grid[2][0] == 'O' or grid[2][0] == 'T':
					if grid[3][0] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[0] = 1
					elif grid[3][0] == 'O' or grid[3][0] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[0][0] == 'T':
			if grid[1][0] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[0] = 1
			elif grid[1][0] == 'X':
				if grid[2][0] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[0] = 1
				elif grid[2][0] == 'X':
					if grid[3][0] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[0] = 1
					elif grid[3][0] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[1][0] == 'O':
				if grid[2][0] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[0] = 1
				elif grid[2][0] == 'O':
					if grid[3][0] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[0] = 1
					elif grid[3][0] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not colEmpty[1]:
		if grid[0][1] == '.':
			incomplete = 1
			rowEmpty[0] = 1
			colEmpty[1] = 1
		elif grid[0][1] == 'X':
			if grid[1][1] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[1] = 1
			elif grid[1][1] == 'X' or grid[1][1] == 'T':
				if grid[2][1] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[1] = 1
				elif grid[2][1] == 'X' or grid[2][1] == 'T':
					if grid[3][1] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[1] = 1
					elif grid[3][1] == 'X' or grid[3][1] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[0][1] == 'O':
			if grid[1][1] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[1] = 1
			elif grid[1][1] == 'O' or grid[1][1] == 'T':
				if grid[2][1] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[1] = 1
				elif grid[2][1] == 'O' or grid[2][1] == 'T':
					if grid[3][1] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[1] = 1
					elif grid[3][1] == 'O' or grid[3][1] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[0][1] == 'T':
			if grid[1][1] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[1] = 1
			elif grid[1][1] == 'X':
				if grid[2][1] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[1] = 1
				elif grid[2][1] == 'X':
					if grid[3][1] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[1] = 1
					elif grid[3][1] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[1][1] == 'O':
				if grid[2][1] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[1] = 1
				elif grid[2][1] == 'O':
					if grid[3][1] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[1] = 1
					elif grid[3][1] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not colEmpty[2]:
		if grid[0][2] == '.':
			incomplete = 1
			rowEmpty[0] = 1
			colEmpty[2] = 1
		elif grid[0][2] == 'X':
			if grid[1][2] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[2] = 1
			elif grid[1][2] == 'X' or grid[1][2] == 'T':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'X' or grid[2][2] == 'T':
					if grid[3][2] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[2] = 1
					elif grid[3][2] == 'X' or grid[3][2] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[0][2] == 'O':
			if grid[1][2] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[2] = 1
			elif grid[1][2] == 'O' or grid[1][2] == 'T':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'O' or grid[2][2] == 'T':
					if grid[3][2] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[2] = 1
					elif grid[3][2] == 'O' or grid[3][2] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[0][2] == 'T':
			if grid[1][2] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[2] = 1
			elif grid[1][2] == 'X':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'X':
					if grid[3][2] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[2] = 1
					elif grid[3][2] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[1][2] == 'O':
				if grid[2][2] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[2] = 1
				elif grid[2][2] == 'O':
					if grid[3][2] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[2] = 1
					elif grid[3][2] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved and not colEmpty[3]:
		if grid[0][3] == '.':
			incomplete = 1
			rowEmpty[0] = 1
			colEmpty[3] = 1
		elif grid[0][3] == 'X':
			if grid[1][3] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[3] = 1
			elif grid[1][3] == 'X' or grid[1][3] == 'T':
				if grid[2][3] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[3] = 1
				elif grid[2][3] == 'X' or grid[2][3] == 'T':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'X' or grid[3][3] == 'T':
						solved = 1
						print "Case #%d: X won" % (game)
		elif grid[0][3] == 'O':
			if grid[1][3] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[3] = 1
			elif grid[1][3] == 'O' or grid[1][3] == 'T':
				if grid[2][3] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[3] = 1
				elif grid[2][3] == 'O' or grid[2][3] == 'T':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'O' or grid[3][3] == 'T':
						solved = 1
						print "Case #%d: O won" % (game)
		elif grid[0][3] == 'T':
			if grid[1][3] == '.':
				incomplete = 1
				rowEmpty[1] = 1
				colEmpty[3] = 1
			elif grid[1][3] == 'X':
				if grid[2][3] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[3] = 1
				elif grid[2][3] == 'X':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'X':
						solved = 1
						print "Case #%d: X won" % (game)
			elif grid[1][3] == 'O':
				if grid[2][3] == '.':
					incomplete = 1
					rowEmpty[2] = 1
					colEmpty[3] = 1
				elif grid[2][3] == 'O':
					if grid[3][3] == '.':
						incomplete = 1
						rowEmpty[3] = 1
						colEmpty[3] = 1
					elif grid[3][3] == 'O':
						solved = 1
						print "Case #%d: O won" % (game)

	if not solved:
		if incomplete:
			print "Case #%d: Game has not completed" % (game)
		else:
			print "Case #%d: Draw" % (game)

	blank = raw_input()