import sys

def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

def valid( string, con ):
	x = 0
	for s in string:
		if s not in 'aeiou':
			x += 1
		else:
			x = 0

		if x >= con:
			return True

	return False		

def find( i, n,  starts ):
	for x in xrange( 0, len( starts ) ):
		if starts[ x ] >= i + n:
			return starts[ x ]

	return -1
	
for t in xrange( input() ):
	value = 0
	s, x = raw_input().split()
	n = int(x)
	starts = []
	length = len( s ) 
	if n <= len( s ):
		for i in xrange( 0, len( s ) - n + 1 ):
			subs = s[ i : i + n ]
			if valid( subs, n ):
				starts.append( i + n )

		for i in xrange( 0, len( s ) - n + 1 ):
			e = find( i, n, starts )
			if e >= 0:
				value += length - e + 1

	print 'Case #' + str(t+1) + ': ' + str( value )
