import sys

sys.stdin.readline()
for c, l in enumerate( sys.stdin.xreadlines() ):
	N, K = map( int, l.split() )
	p = 2 ** N
	print "Case #%d:" % ( c+1, ),
	if K % p == p - 1:
		print "ON"
	else:
		print "OFF"
