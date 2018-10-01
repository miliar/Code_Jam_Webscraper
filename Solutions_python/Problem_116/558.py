import time
import itertools

f = open("in.txt")
T = int(f.readline())
isDraw = True
result = {
	'1': "X won",
	'2': "O won",
	'0': "Draw",
	'3': "Game has not completed"
}
ans = 0
row = [''] * 4

def check(string):
	global ans
	global isDraw

	countX = string.count('X')
	countO = string.count('O')
	countT = string.count('T')
	# print string, countX, countO, countT
	if ( countX == 4 or (countX >=3 and countT > 0) ): ans = 1
	if ( countO == 4 or (countO >=3 and countT > 0) ): ans = 2
	if string.count('.') > 0: isDraw = False
	# print ans

def checkCol(i):
	string = ""
	for r in range(4): string += row[r][i]
	check(string)

def checkDiag():
	string1 = ""
	string2 = ""
	for i in range(4):
		string1 += row[i][i]
		string2 += row[i][3-i]
	check(string1)
	check(string2)

for case in range( T ):
	start = int(time.time())
	
	ans = 0
	isDraw = True

	for i in range(4):
		row[i] = f.readline()
		check( row[i] )
	f.readline()

	for i in range(4):
		checkCol(i)
	checkDiag()

	if ans == 0 and not isDraw: ans = 3

	print "Case #{}: {}".format( case+1, result[str(ans)] )

	# print int(time.time()) - start