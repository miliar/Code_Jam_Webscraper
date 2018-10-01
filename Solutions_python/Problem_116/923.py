# Python 2.7.2 (341e1e3821fff77db3bb5cdb7a4851626298c44e, Nov 23 2012, 19:06:15)
# [PyPy 1.9.0] on darwin
# (C) 2013 Dennis Bliefernicht

BASENAME="A"
TYPE="ex"
TYPE="sm0"
TYPE="la"
NODOUT=False



def checkwin(row):
	c = None
	for x in row:
		if x == ".":
			return None
		elif x == "T":
			continue
		elif c != None and x != c:
			return None
		else:
			c = x
	return c

def process():
	row = [pop(), pop(), pop(), pop()]
	pop()
	win = None

	win1 = checkwin([row[0][0], row[1][1], row[2][2], row[3][3]])
	win2 = checkwin([row[0][3], row[1][2], row[2][1], row[3][0]])

	if win1:
		win = win1
	elif win2:
		win = win2
	
	if not win:
		for x in range(4):
			crow = checkwin([row[0][x], row[1][x], row[2][x], row[3][x]])
			ccol = checkwin([row[x][0], row[x][1], row[x][2], row[x][3]])
			
			if crow:
				win = crow
				break
			if ccol:
				win = ccol
				break
		
	if not win:
		for r in row:
			if "." in r:
				return "Game has not completed"
	else:
		if win == "X":
			return "X won"
		elif win == "O":
			return "O won"
	
	return "Draw"

# ------------------------------------
# GCJ2013 framework stuff
# ------------------------------------
import time

lines = []
outf = None

def pop():
	global lines
	e = lines[0]
	lines = lines[1:]
	return e
	
def popint():
	return int(pop())
	
def popflt():
	return float(pop())
	
def popintarray():
	return map(lambda x: int(x), pop().split(" "))

def popstrarray():
	return pop().split(" ")
	
def outstr(s):
	global outf
	print s
	outf.write(s + "\n")

def dout(*vals):
	if NODOUT:
		return
	print "%",
	for v in vals:
		print str(v),
	print
	
def main():
	global lines
	case_count = int(pop())
	for case_number in range(case_count):
		result = process()
		outstr("Case #%d: %s" % (case_number+1, result))
	if len(lines) != 0:
		print "! %d lines remaining" % (len(lines))

if __name__ == "__main__":
	fname = BASENAME
	if TYPE[0:2] == "sm":
		fname += "-small"
		if len(TYPE) > 2:
			fname += "-attempt" + TYPE[2:]
	elif TYPE == "la":
		fname += "-large"

	f = open(fname + ".in", "r")
	lines = map(lambda x: x[:-1], f.readlines())
	f.close()
	
	outf = open(fname + ".out", "w")
	timebefore = time.time()
	main()
	timeafter = time.time()
	outf.close()
	
	runtime = timeafter - timebefore
	print "%% Runtime: %dm%2.3fs" % (int(runtime / 60), runtime % 60)
	