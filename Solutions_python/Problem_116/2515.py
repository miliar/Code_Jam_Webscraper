src = file( "input4", "rb" )
dest = file( "Output", 'w' )
content = ""
lines = src.readlines()


for z in range( 0, (int)(lines[0]) ):
	begin_line = z * 5 + 1
	gameResult = None
	# check each row
	for j in range( begin_line, begin_line + 4):
		x , o = 0, 0
		for k in range( 0, 4 ):
			if lines[j][k] == 'O':
				o+=1
			elif lines[j][k] == 'X':
				x+=1
			elif lines[j][k] == 'T':
				o+=1
				x+=1
		if x == 4:
			gameResult = 'X'
			break
		elif o == 4:
			gameResult = 'O'
			break

	# check each column
	if gameResult == None:
		for j in range( 0, 4):
			x, o = 0, 0
			for k in range( begin_line, begin_line + 4):
				if lines[k][j] == 'O':
					o+=1
				elif lines[k][j] == 'X':
					x+=1
				elif lines[k][j] == 'T':
					o+=1
					x+=1
			if x == 4:
				gameResult = 'X'
				break
			elif o == 4:
				gameResult = 'O'
				break

	# check diagonals
	if gameResult == None:
		x, o = 0, 0
		for i in range( 0, 4 ):
			if lines[ begin_line + i ][ i ] == 'O':
				o+=1
			elif lines[ begin_line + i ][ i ] == 'X':
				x+=1
			elif lines[ begin_line + i ][ i ] == 'T':
				o+=1
				x+=1
		if x == 4:
			gameResult = 'X'
		elif o == 4:
			gameResult = 'O'

	if gameResult == None:
		x, o = 0, 0
		for i in range( 0, 4 ):
			if lines[ begin_line + i ][ 3-i ] == 'O':
				o+=1
			elif lines[ begin_line + i ][ 3-i ] == 'X':
				x+=1
			elif lines[ begin_line + i ][ 3-i ] == 'T':
				o+=1
				x+=1
		if x == 4:
			gameResult = 'X'
		elif o == 4:
			gameResult = 'O'

	# determing the result
	if gameResult == None:
		d = 0
		for j in range( begin_line, begin_line + 4):
			
			for k in range( 0, 4 ):
				if lines[j][k] == '.':
					d+=1
		if d != 0:
			content += "Case #%d: Game has not completed"%(z+1)
		else:
			content += "Case #%d: Draw"%(z+1)
	else:
		content += "Case #%d: %c won"%(z+1, gameResult)
	if  (z+1) != (int)(lines[0]):
		content += '\n'

# for line in lines:
# 	line = line.strip('\n')
# 	content += line

dest.write( content )
