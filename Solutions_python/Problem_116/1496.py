import sys

def checkLine(line, player):
	return len(filter(lambda c : c == player or c == "T", line)) == 4

with open(sys.argv[1]) as f:
	content = f.readlines()
	
	count = int(content[0])

	for i in range(0, count):
		arr = [content[j] for j in range(5*i + 1, 5*i + 5)]
		
		# rows, columns, diagonal 1, diagonal 2
		lines = [arr[y].strip() for y in range(0,4)] \
			+ [[arr[y][x] for y in range(0,4)] for x in range(0,4)] \
			+ [[arr[x][y] for (x,y) in [(0,0), (1,1), (2,2), (3,3)]]] \
			+ [[arr[x][y] for (x,y) in [(0,3), (1,2), (2,1), (3,0)]]]
		
		xwon = any([checkLine(l, "X") for l in lines])
		owon = any([checkLine(l, "O") for l in lines])
		complete = not any(["." in line for line in arr])
		
		result = "Case #" + str(i + 1) + ": "
		
		if xwon:
			result += "X won"
		elif owon:
			result += "O won"
		elif complete:
			result += "Draw"
		else:
			result += "Game has not completed"
			
		print(result)