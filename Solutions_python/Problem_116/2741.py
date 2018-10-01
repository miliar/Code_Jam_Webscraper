import string
infile = file("A-small-attempt0.in")
linebuff = infile.readline()
caseamount = string.atoi(linebuff)
for cases in xrange(caseamount):
	board = [ None, None, None, None ]
	for x in xrange(4):
		linebuff = infile.readline()
		#print linebuff,
		board[x] = []
		
		for y in xrange(4):
			board[x].append(linebuff[y])

	linebuff = infile.readline()
#	print board
	
	result = 'D'
	
	#test diagnal
	lastsymbol = 'T'
	for i in xrange(4):
		if board[i][i] == 'O':
			if lastsymbol == 'X':
					break
			lastsymbol = 'O'
			continue
		elif board[i][i] == 'X':
			if lastsymbol == 'O':
				break
			lastsymbol = 'X'
			continue
		elif board[i][i] == '.':
			result = '.'
			break
	else:
		if lastsymbol == 'O':
			result = 'O'
		elif lastsymbol == 'X':
			result = 'X'
		
	
	#test antidiagnal
	if result == 'D' or result == '.':
		lastsymbol = 'T'
		for i in xrange(4):
			if board[i][3-i] == 'O':
				if lastsymbol == 'X':
					break
				lastsymbol = 'O'
				continue
			elif board[i][3-i] == 'X':
				if lastsymbol == 'O':
					break
				lastsymbol = 'X'
				continue
			elif board[i][3-i] == '.':
				result = '.'
				break
		else:
			if lastsymbol == 'O':
				result = 'O'
			elif lastsymbol == 'X':
				result = 'X'
	
	if result == 'D' or result == '.':
		for x in xrange(4):
			# testrows
			lastsymbol = 'T'
			for y in xrange(4):
				if board[x][y] == 'O':
					if lastsymbol == 'X':
						break
					lastsymbol = 'O'
					continue
				elif board[x][y] == 'X':
					if lastsymbol == 'O':
						break
					lastsymbol = 'X'
					continue
				elif board[x][y] == '.':
					result = '.'
					break
			else:
				if lastsymbol == 'O':
					result = 'O'
					break
				elif lastsymbol == 'X':
					result = 'X'
					break
			
			if result == 'O' or result == 'X':
				break;
			
			
			# testcols
			lastsymbol = 'T'
			for y in xrange(4):
				if board[y][x] == 'O':
					if lastsymbol == 'X':
						break
					lastsymbol = 'O'
					continue
				elif board[y][x] == 'X':
					if lastsymbol == 'O':
						break
					lastsymbol = 'X'
					continue
				elif board[y][x] == '.':
					result = '.'
					break
			else:
				if lastsymbol == 'O':
					result = 'O'
					break
				elif lastsymbol == 'X':
					result = 'X'
					break
			
			if result == 'O' or result == 'X':
				break;
	
	#print result
	if result == '.':
		print "Case #"+str(cases+1)+": Game has not completed"
	if result == 'D':
		print "Case #"+str(cases+1)+": Draw"
	elif result == 'X' or result == 'O':
		print "Case #"+str(cases+1)+": "+str(result)+" won"
	
	