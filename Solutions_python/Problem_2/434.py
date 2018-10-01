#!/usr/bin/env python
import datetime

def _is_reusable( arrival_time, tt_opposite, ta_time ) :

	next_departure_time_hour = arrival_time.hour + ta_time / 60
	next_departure_time_minute = arrival_time.minute + ta_time % 60
	if next_departure_time_minute >= 60 :
		next_departure_time_hour += 1
		next_departure_time_minute -= 60

	next_departure_time = datetime.time( next_departure_time_hour, next_departure_time_minute )

	for i, opposite_departure in enumerate(tt_opposite) :
		if next_departure_time <= opposite_departure[0] :
			if opposite_departure[1] == False  :
				# do resue
				tt_opposite[i][1] = True # mark as already reused
				return True, tt_opposite
	return False, tt_opposite

def get_necessary_train( tt_a, tt_b, ta_time ) :
	num_a = len(tt_a)
	num_b = len(tt_b)

	# sort time table first
	tt_a = sorted(tt_a)
	tt_b = sorted(tt_b)
	#print tt_a
	#print tt_b
	# do reduce if reusable

	# make opposite list for A (=B)
	opposite = [ [i[0],0] for i in tt_b ]
	#print 'B-depart', opposite
	for i in tt_a :
		#print 'is_reusable:', i[1], opposite
		successfalse, opposite = _is_reusable( i[1], opposite, ta_time ) 
		if successfalse :
			num_b -= 1
	# make opposite list for B (=A)
	opposite = [ [i[0],0] for i in tt_a ]
	#print 'A-depart', opposite
	for i in tt_b :
		successfalse, opposite = _is_reusable( i[1], opposite, ta_time )
		if successfalse :
			num_a -= 1


	return num_a, num_b

def time_table( num_of_train, file ) :

	time_table = []
	# assume 1900-1-1, and use time module
	for i in range(num_of_train) :
		# get start and arrive time in a day
		s_time_str, a_time_str = file.readline().rstrip().split()
		s_time_hour, s_time_minute = [int(i) for i in s_time_str.split(':')]
		a_time_hour, a_time_minute = [int(i) for i in a_time_str.split(':')]

		s_time = datetime.time( s_time_hour, s_time_minute )
		a_time = datetime.time( a_time_hour, a_time_minute )
		time_table.append( [s_time, a_time] )
	
	return time_table

def solve_single( prob_num, file ) :

	ta_time = int( file.readline() )

	num_from_a, num_from_b = file.readline().rstrip().split()
	num_from_a = int(num_from_a)
	num_from_b = int(num_from_b)

	#print num_from_a, num_from_b

	time_table_from_a = time_table( num_from_a, file )
	time_table_from_b = time_table( num_from_b, file )

	train_from_a, train_from_b = get_necessary_train( time_table_from_a, time_table_from_b, ta_time )

	#test 
	#print 'ta_time:', ta_time
	#print time_table_from_a
	#print time_table_from_b
	print 'Case #%d: %d %d' % (prob_num, train_from_a, train_from_b)

def solve( file_name ) :
	file = open( file_name , 'r' )

	num_of_cases = int( file.readline() )

	for i_prob in range(num_of_cases) :
		solve_single( i_prob+1, file )

if __name__ == '__main__' :

	solve( 'B-small-attempt0.in' )
