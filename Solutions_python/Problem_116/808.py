infile = open("input.txt", "r")
outfile = open("output.txt", "w")

def check(seq, who):
	for j in seq:
		win = True
		for i in j:
			if i != who and i != 'T':
				win = False
		if win:
			return True
	return False

ncases = int(infile.readline())
for case in xrange(ncases):
	board = []
	xwin = False
	owin = False
	for row in xrange(0, 4):
		board.append(infile.readline().strip())

	infile.readline()
	for i in xrange(0, 4):
		test = [board[i], [board[j][i] for j in xrange(0, 4)], [board[j][j] for j in xrange(0, 4)], [board[j][3-j] for j in xrange(0, 4)]]
		if check(test, 'X'):
			xwin = True
		if check(test, 'O'):
			owin = True

	if xwin:
		print >>outfile, "Case #%d: X won" % (case+1)
	elif owin:
		print >>outfile,"Case #%d: O won" % (case+1)
	else:
		empty = [board[i][j]=='.' for i in xrange(4) for j in xrange(4)]
		truths = [x for x in empty if x]
		if len(truths)>0:
			print >>outfile, "Case #%d: Game has not completed" % (case+1)
		else:
			print >>outfile, "Case #%d: Draw" % (case+1)

infile.close()
outfile.close()