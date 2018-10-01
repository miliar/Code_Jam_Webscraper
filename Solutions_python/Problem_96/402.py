t = int ( raw_input() )
for i in range (t):
	strng = raw_input().split()
	out = 0
	supr = 0
	n = int ( strng [0] )
	s = int ( strng [1] )
	p = int ( strng [2] )
	for j in ( strng [3:] ) :
		j = int ( j )
		if (j == 0):
			if (p ==0):
				out += 1
		elif ( ( (j/3) + (j%3) ) >= p ):
			if( (j/3) <= (p-2) ):
				supr += 1
			else:
				out += 1
		elif ( j == ( p-1 )*3 ):
			supr += 1
	out += min(supr,s)
	print ( "Case #"+ str(i+1) + ": " + str( out ) )
