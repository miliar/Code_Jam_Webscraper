#!/usr/bin/env python
# -*- coding:Utf-8 -*-

with open( "A-large.in", "rt" ) as fileInput :
	with open( "output.txt", "wt" ) as fileOutput :
		t = int( fileInput.readline() )
		for i in range( 1, t + 1 ):
			bPosition = 1
			oPosition = 1
			line = ( fileInput.readline() ).split( " " )
			n = int( line[ 0 ] )
			oMoves = []
			bMoves = []
			for j in range( n ):
				if( line[ 2 * j + 1 ] == 'O' ):
					oMoves.append( ( j, int( line[ 2 * j + 2 ] ) ) )
				else:
					bMoves.append( ( j, int( line[ 2 * j + 2 ] ) ) )
			ca   = 0 # Current action
			time = 0
			while( oMoves or bMoves ):
				oDoAction = False
				# O push button
				if( oMoves and oMoves[ 0 ][ 0 ] == ca and oMoves[ 0 ][ 1 ] == oPosition ):
					del oMoves[ 0 ]
					ca += 1
					oDoAction = True
				else:
					# O move
					if( oMoves and oMoves[ 0 ][ 1 ] > oPosition ):
						oPosition += 1
					else:
						if( oMoves and oMoves[ 0 ][ 1 ] < oPosition ):
							oPosition -= 1
				# B push button		
				if( not oDoAction and bMoves and bMoves[ 0 ][ 0 ] == ca and bMoves[ 0 ][ 1 ] == bPosition ):
					del bMoves[ 0 ]
					ca += 1
				else:
					# B move
					if( bMoves and bMoves[ 0 ][ 1 ] > bPosition ):
						bPosition += 1
					else:
						if( bMoves and bMoves[ 0 ][ 1 ] < bPosition ):
							bPosition -= 1
				# Increment time
				time += 1
			# Write result
			fileOutput.write( "Case #%d: %d\n" %( i, time ) )

