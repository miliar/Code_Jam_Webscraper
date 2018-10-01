import string
import sys

file = sys.argv[1]

input = open(file, 'r')
output = open(file + ".out", 'w')

testcases = int(input.readline())

i = 0

cheat = 0
magic = 0
win = 0

while i < testcases:
	row = int(input.readline())
	board1 = []
	for x in range (0, 4):
		board1.append(string.split(input.readline()[0:-1], " "))
	col = int(input.readline())
	board2 = []
	for x in range (0, 4):
		board2.append(string.split(input.readline()[0:-1], " "))
	
	board1[row - 1] = sorted(board1[row - 1])
	board2[col - 1] = sorted(board2[col - 1])
	possible = [val for val in board1[row - 1] if val in board2[col - 1]]
	
	
	if len(possible) == 0:
		out = "Volunteer cheated!"
		cheat += 1
	elif len(possible) == 1:
		out = possible[0]
		win += 1
	else:
		out = "Bad magician!"
		magic += 1
	
	i += 1
	
	output.write("Case #" + str(i) + ": " + str(out)+'\n')
	print board1[row - 1]
	print board2[col - 1]
	print possible
	print "Case #" + str(i) + ": " + str(out)+'\n'
	print ""
print cheat
print magic
print win
