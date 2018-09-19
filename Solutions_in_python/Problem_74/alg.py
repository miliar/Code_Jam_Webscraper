# returns the next button to be pressed by bot "bot"
def findNextBotMove(q, bot):
	for mbot, mbutton in q:
		if bot == mbot:
			return (mbot, mbutton)
	return None

# q is a list of tuples(bot, button)
def solve(q):
	numMoves = 0

	opos = 1
	bpos = 1

	while len(q) > 0:
		q, opos, bpos = doMove(q, opos, bpos)
		numMoves += 1
	
	#print numMoves
	return numMoves

def sgn(x):
	if x > 0:
		return 1
	elif x < 0:
		return -1
	else:
		return 0

def doMove(q, opos, bpos):
	nextMove = q[0]
	omove = findNextBotMove(q, "O")
	bmove = findNextBotMove(q, "B")

	if omove == None:
		omove = ("O", opos)
	if bmove == None:
		bmove = ("B", bpos)

	odt = sgn(omove[1] - opos)
	bdt = sgn(bmove[1] - bpos)

	# special case : both bots are at their correct positions
	if odt == 0:
		if nextMove[0] == "O":
			odesc = "Push button %s" % omove[1]
			q = q[1:]
		else:
			odesc = "Wait at button %s" % opos
		nextopos = opos
	else:
		odesc = "Move to button %s" % (opos + odt)
		nextopos = opos + odt

	if bdt == 0:
		if nextMove[0] == "B":
			bdesc = "Push button %s" % bmove[1]
			q = q[1:]
		else:
			bdesc = "Wait at button %s" % bpos
		nextbpos = bpos
	else:
		bdesc = "Move to button %s" % (bpos + bdt)
		nextbpos = bpos + bdt

	#print "%20.20s | %20.20s" % (odesc, bdesc)
	return q, nextopos, nextbpos
	
