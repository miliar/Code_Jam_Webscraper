def counts (iterable):
	x = len ([e for e in iterable if e == "X"])
	o = len ([e for e in iterable if e == "O"])
	t = len ([e for e in iterable if e == "T"])
	dot = len ([e for e in iterable if e == "."])

	return (x,o,t,dot)

def check_ongoing (iterable):
	for row in iterable:
		if "." in row:
			return True
	return False

def checkdiags (iterable):
	diag1 = [iterable[i][i] for i in range (4)]
	x,o,t,dot = counts (diag1)
	if x == 4 or (x == 3 and t == 1):
		return "X won"
	elif o == 4 or (o == 3 and t == 1):
		return "O won"
	
	diag2 = [iterable[3-i][i] for i in range (4)]
	x,o,t,dot = counts (diag2)
	if x == 4 or (x == 3 and t == 1):
		return "X won"
	elif o == 4 or (o == 3 and t == 1):
		return "O won"

	return None

def checkrows (rno, iterable):
	row = iterable [rno]
	
	x,o,t,dot = counts (row)
	if x == 4 or (x == 3 and t == 1):
		return "X won"
	elif o == 4 or (o == 3 and t == 1):
		return "O won"
	
	return None

def checkcols (cno, iterable):
	col = [iterable[i][cno] for i in range (4)]

	x,o,t,dot = counts (col)
	if x == 4 or (x == 3 and t == 1):
		return "X won"
	elif o == 4 or (o == 3 and t == 1):
		return "O won"
	
	return None

def check_helper (tests, test):
	for row in range (4):
		a = checkrows (row, tests[test])
		if not a == None:
			return a
		b = checkcols (row, tests[test])
		if not b == None:
			return b
	c = checkdiags (tests[test])
	if not c == None:
		return c
	d = check_ongoing (tests[test])
	if d:
		return "Game has not completed"
	else:
		return "Draw"

def check (tests):
	output = []
	for test in tests:
		output.append (check_helper(tests, test))
	return output

def read ():
	ntests = input ()
	tests = {}
	for test in range (ntests):
		for lno in range (4):
			line = raw_input ()
			if test in tests:
				tests[test].append (line.strip())
			else:
				tests[test] = []
				tests[test].append (line.strip())
		ignore = raw_input()
	return tests

def write (output):
	for i in range (len (output)):
		print "Case #" + str (i+1) + ": " + output[i]

if __name__ == "__main__":
	tests = read ()
	output = check (tests)
	write (output)
