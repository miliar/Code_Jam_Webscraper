#!/usr/bin/python

def to_mins( time ) :
	time = time.split(':')
	return int(time[0])*60 + int(time[1])


def get_cases( file_name ) :
	cases = []
	file_in = open(file_name , "r").read().split('\n')
	i = 0
	ncases = int(file_in[i])
	i+=1
	for c in range(ncases):
		line = file_in[i]
		turn = int(line)
		i+=1		
		line = file_in[i].split(' ')
		ta = int(line[0])
		tb = int(line[1])
		i+=1
		from_a = []
		to_b = []
		from_b = []
		to_a = []
		for aux in range(ta) :
			line = file_in[i+aux].split(' ')
			from_a.append( to_mins(line[0]) )
			to_b.append( to_mins(line[1])+turn )
		i+=ta
		for aux in range(tb) :
			line = file_in[i+aux].split(' ')
			from_b.append( to_mins(line[0]) )
			to_a.append( to_mins(line[1])+turn )
		i+=tb
		cases.append( ( from_a , from_b , to_a , to_b ) )

	return cases	

def cant_times( time , l_time ) :
	c = 0
	for el in l_time :
		if el == time :
			c +=1
	return c

def trains( from_a , from_b , to_a , to_b ) :
	in_a = 0
	in_b = 0
	a = 0
	b = 0
	for time in range( 24 * 60 ) :
		if time in to_a :
			in_a += cant_times( time , to_a )
		if time in to_b :
			in_b += cant_times( time , to_b )
		if time in from_a :
			if in_a == 0 :
				a += cant_times( time , from_a )
			else :
				in_a -= cant_times( time , from_a )
				if in_a < 0 :
					a+= abs(in_a)
					in_a = 0
		if time in from_b :
			if in_b == 0 :
				b += cant_times( time , from_b )
			else :
				in_b -= cant_times( time , from_b )
				if in_b < 0 :
					b+= abs(in_b)
					in_b = 0
	
	return a , b


cases = get_cases( "B-large.in" )

output = ""
for i in range(len( cases )) :				
	a , b = trains( cases[i][0] , cases[i][1] , cases[i][2] , cases[i][3] )
	output += "Case #%d: %d %d \n" % ( i+1 , a , b )

file_out = file("out.out" , "w" )
file_out.write( output ) 
file_out.close()


