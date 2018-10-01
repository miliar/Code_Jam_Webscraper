#!/usr/bin/python

def readline( f ):
	line = f.readline()
	line = line[:-1]
	return line

def read_integer( f ):
	string = readline( f )
	return int( string )

def read_integer_list( f ):
	string = readline( f )
	string_list = string.split( " " )

	for i in range( len( string_list ) ):
		string_list[i] = int( string_list[i] )

	return string_list

def read_char_list( f ):
	string = readline( f )

	char_list = []
	for i in range( len( string ) ):
		char_list.append( string[i] )

	return char_list

def has_empty_fields( f ):
	for x in range( 4 ):
		for y in range( 4 ):
			if fields[x][y] == ".":
				return True

	return False

def get_winner( r ):
	player = None
	for f in r:
		if f == 'T':
			continue
		if f == '.':
			return None

		if player is None:
			player = f
		elif player != f:
			return None

	return player

f = open( "A-large.in", "r" )
test_cases = read_integer( f )

for i in range( test_cases ):
	fields = []
	fields.append( read_char_list( f ) )
	fields.append( read_char_list( f ) )
	fields.append( read_char_list( f ) )
	fields.append( read_char_list( f ) )

	# read trailing blank line
	readline( f )

	winner = None

	# try horizontal
	for r in fields:
		print
		if get_winner( r ) is not None:
			winner = get_winner( r )
			break

	# try vertical
	for y in range( 4 ):
		r = [ fields[0][y], fields[1][y], fields[2][y], fields[3][y] ]

		if get_winner( r ) is not None:
			winner = get_winner( r )
			break

	# try diagonal
	x = y = 0
	row_a = []
	row_b = []
	for j in range( 4 ):
		row_a.append( fields[x][y] )
		row_b.append( fields[3-x][y] )

		x += 1
		y += 1

	if get_winner( row_a ) is not None:
		winner = get_winner( row_a )
	elif get_winner( row_b ) is not None:
		winner = get_winner( row_b )

	result = None
	if winner is not None:
		result = winner + " won"
	elif has_empty_fields( fields ):
		result = "Game has not completed"
	else:
		result = "Draw"

	print( "Case #" + str( i + 1 ) + ": " + result )