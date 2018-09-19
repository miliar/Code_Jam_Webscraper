import sys

data = sys.argv[1]

f = open(data,'r')
data = f.read()

tests = data.split("\n")

# Cut the first and last lines off
tests = tests[1:len(tests)-1]

data = ("\n").join(tests)

tests = data.split("\n\n")
exit


def testGame(game, check, check2=""):

	# Rows
	for row in [0,1,2,3]:
		rows = 0
		for i in range(row*4,row*4+4):
			if game[i] == check or game[i] == "T":
				rows += 1
		if rows == 4:
			return True

	#columns
	for column in [0,1,2,3]:
		columns = 0
		for j in range(0,4):
			i = j*4 + column
			if game[i] == check or game[i] == "T":
				columns += 1
		if columns == 4:
			return True

	#diagonal
	diagonal = 0
	for i in [0,5,10,15]:
		if game[i] == check or game[i] == "T":
			diagonal += 1
		else:
			break
	if diagonal == 4:
		return True 

	#diagonal 2
	diagonal = 0
	for i in [3,6,9,12]:
		if game[i] == check or game[i] == "T":
			diagonal += 1
		else:
			break
	if diagonal == 4:
		return True 

	return False



case = 0
for test in tests:
	case += 1
	test = "".join(test.split("\n"))
	
	print "Case #%s:" % (case),

	if testGame(test, "X"):
		print "X won"
	elif testGame(test, "O"):
		print "O won"
	elif not ("." in test):
		print "Draw"
	else:
		print "Game has not completed"

