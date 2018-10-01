from sys import *

lines = stdin.read().replace('\r',"").split('\n')
ntests = int(lines.pop(0))

for testno in range(1,ntests+1):
	first = int(lines.pop(0))-1
	board = []
	for row in range(4):
		board.append(lines.pop(0).split(' '))
	possible = set(board[first])
	second = int(lines.pop(0))-1
	board = []		
	for row in range(4):
		board.append(lines.pop(0).split(' '))
	result = possible&set(board[second])
#	print result
	stdout.write("Case #"+str(testno)+": ")
	if len(result) > 1: 
		stdout.write("Bad magician!\n")
	elif len(result) == 0:
		stdout.write("Volunteer cheated!\n")
	else:
		stdout.write(str(result.pop())+'\n')

