#!/usr/bin/env python
# -*- coding:Utf-8 -*-

def intToBin( i ):
	binL = []
	while( i > 0 ):
		binL.append( i % 2 )
		i = i >> 1
	return binL

def binToInt( l ):
	i   = 0
	two = 1
	for elmt in l:
		i   += elmt * two
		two *= 2
	return i

def binFakeSum( binA, binB ):
	binApB = []
	lenA   = len( binA )
	lenB   = len( binB )
	i      = 0
	
	while( i < lenA and i < lenB ):
		if( binA[ i ] == 0 and binB[ i ] == 0 ):
			binApB.append( 0 )
		elif( binA[ i ] == 1 and binB[ i ] == 0 ):
			binApB.append( 1 )
		elif( binA[ i ] == 0 and binB[ i ] == 1 ):
			binApB.append( 1 )
		else:
			binApB.append( 0 )
		i += 1
	
	if( lenA != lenB ):
		if(	i == lenA ):
			binApB.extend( binB[ i : ] )
		else:	
			binApB.extend( binA[ i : ] )
			
	return binApB

def listSum( l ):
	return sum( l )
	
def listFakeSum( l ):
	iBin = intToBin( 0 )
	for elmt in l:
		iBin = binFakeSum( iBin, intToBin( elmt ) )
	return binToInt( iBin )
		
def generateSet( l ):
	gs = []
	for i in range( 1 <<  len( l ) ):
		tmp1 = []
		tmp2 = []
		for j in range( len ( l ) ):
			if( i & ( 1 << j ) ):
				tmp1.append( l[ j ] )
			else:
				tmp2.append( l[ j ] )
		gs.append( ( tmp1, tmp2 ) )
	return gs

with open( "C-small-attempt2.in", "rt" ) as fileInput :
	with open( "output.txt", "wt" ) as fileOutput :
		t = int( fileInput.readline() )
		for i in range( 1, t + 1 ):
			n    = int( fileInput.readline() )
			ci   = map( int, ( fileInput.readline() ).split( " " ) )
			best = 0
			gs   = generateSet( ci )
			for ( l1, l2 ) in gs[ : len( gs ) / 2 ]:
				if( l1 and l2 ):
					v1 = listFakeSum( l1 )
					v2 = listFakeSum( l2 )
					if( v1 == v2 ):
						sol = max( listSum( l1 ), listSum( l2 ) )
						if( sol > best ):
							best = sol 
			
			if( best == 0 ):
				fileOutput.write( "Case #%d: NO\n" %( i ) )
			else:
				fileOutput.write( "Case #%d: %d\n" %( i, best ) )
