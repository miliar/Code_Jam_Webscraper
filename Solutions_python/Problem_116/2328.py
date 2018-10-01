numOfTestCase = int(raw_input())

for testCase in range(1, (numOfTestCase+1)):
	if testCase > 1:
		raw_input()
	board = []
	for i in range(4):
		board.append(raw_input())

	status = {'.':False, 'X':False, 'O':False}
	
	#Check row wise is X or O win?
	for row in range(4):
		if board[row][0] == 'T':
			player = board[row][1]
		else :
			player = board[row][0]
		if player != '.':
			for col in range(4):
				if board[row][col] != 'T' and board[row][col] != player:
					break
			else:
				print "Case #" + str(testCase) + ": " + player + " won"  
				status[player] = True
				break
			
	if status[player]:
		continue
		
	for col in range(4):
		if board[0][col] == 'T':
			player = board[1][col]
		else :
			player = board[0][col]
		if player != '.':
			for row in range(4):
				if board[row][col] != 'T' and board[row][col] != player:
					break
			else:
				print "Case #" + str(testCase) + ": " + player + " won"
				status[player] = True
				break
				
	if status[player]:
		continue
		
	if board[0][0] == 'T':
		player = board[1][1]
	else :
		player = board[0][0]
	
	if player != '.':
		for digonal in range(4):
			if board[digonal][digonal] != 'T' and board[digonal][digonal] != player:
				break
		else:
			print "Case #" + str(testCase) + ": " + player + " won"
			continue
		
	if board[0][3] == 'T':
		player = board[1][2]
	else :
		player = board[0][3]
	
	if player != '.':
		for row, col in zip(range(4), range(3,  -1, -1)):
			if board[row][col] != 'T' and board[row][col] != player:
				break
		else:
			print "Case #" + str(testCase) + ": " + player + " won"
			continue
		
	for row in range(4):
		for col in range(4):
			if board[row][col] == '.':
				status['.'] = True
				print "Case #" + str(testCase) + ": Game has not completed"
				break
		if status['.']:
			break
	else:
		print "Case #" + str(testCase) + ": Draw"
