

finput = open("A-large (1).in","r")
foutput = open("A-large (1).out","w")	


def check(h1,h2,H1,H2):
	if ( h1 < H1 and h2 > H2  ):
		return True

	if ( h1 > H1 and h2 < H2  ):
		return True

	return False
	
				 
	

T = int ( (finput.readline()).strip() )
lineno = 1

while ( T > 0) :
	N = int ( (finput.readline()).strip())
	data = []
	count = 0
	for i in range(N):
		## wire 
		inline = (finput.readline()).strip()
		splitline  = inline.split()
		splitline[0] =  int(splitline[0])
		splitline[1] =  int(splitline[1])
		data.append(splitline)
	
	for i in range(N):
		h1 = data[i][0]
		h2 = data[i][1]
		for j in range(i):
			H1 = data[j][0]
			H2 = data[j][1]
			#print "fist " , h1,h2
			#print "fist " , H1,H2
			if ( check(h1,h2, data[j][0],data[j][1])   ):
				
				count = count + 1		
				
			
	#print data
	#print "count = " , count		
	
			
	s =  "Case #%s: %s\n" % ( lineno ,count )
	print s,
	foutput.write(s)
	
	lineno = lineno + 1	
	T = T - 1

    	









	    
    
