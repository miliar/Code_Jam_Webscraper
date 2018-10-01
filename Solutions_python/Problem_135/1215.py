f = open('magic.in')
r = f.readlines()
f.close()

def lines_to_board(lines):
	board = []
	for line in lines:
		board.append(line.strip().split(" "))
	return board

def find_intersection(a, b):
	possibilities = []
	for x in a:
		if x in b:
			possibilities.append(x)
	y = len(possibilities)
	if(y > 1):
		return "Bad magician!"
	elif(y == 1):
		return possibilities[0]
	else:
		return "Volunteer cheated!"

answers = []

num_cases = int(r[0].strip())
curr = 1
while(num_cases != 0):
	first_row_num = int(r[curr].strip())
	curr += 1
	first_board = lines_to_board(r[curr:(curr+4)])
	curr += 4

	second_row_num = int(r[curr].strip())
	curr += 1
	second_board = lines_to_board(r[curr:(curr+4)])
	curr += 4

	answers.append(find_intersection(first_board[first_row_num-1],second_board[second_row_num-1]))
	num_cases-=1
### END WHILE

f = open('magic.out', 'w')
case = 1
for answer in answers:
	f.write("Case #{0}: {1}\n".format(case, answer))
	case+=1
f.close()