# ___ ______________________________________________ ___ #
#|_/*|                                              |*\_|#
#|_/*|    Google Code Jam - "Hello World"           |*\_|#
#|_/*|    10.04.2015 - the end                      |*\_|#
#|_/*|    Qualification                             |*\_|#
#|_/*|______________________________________________|*\_|#
#|                                                      |#
#|        Denis Werner                                  |#
#|______________________________________________________|#
#                                                        #


filename = "D-large.in"
filename = "D-small-attempt1.in"

lines = ()
with open(filename) as file:
	lines = file.read().splitlines()

number_of_sets = int(lines[0])

with open(filename+".solved","w") as outputfile:
	for i in range(0,number_of_sets):


		current_line = lines[i+1]
		print current_line
		X = int(current_line[:current_line.index(" ")])
		current_line = current_line[current_line.index(" ")+1:]
		R = int(current_line[:current_line.index(" ")])
		current_line = current_line[current_line.index(" ")+1:]
		C = int(current_line)

		min_X = {1:1,2:1,3:2,4:2,5:3,6:3}
		max_X = {1:1,2:2,3:2,4:3,5:3,6:4}
		F_max = {1:1,2:2,3:4,4:6,5:9,6:12}

		winner = "RICHARD"
		
		if X > 6:
			winner = "RICHARD"
			print "X too big"
		elif X == 1:
			winner = "GABRIEL"
			print "X = 1"
		elif max(R,C) < X:
			winner = "RICHARD"
			print "max RC < X"
		elif ((R*C)%X) > 0 :
			winner = "RICHARD"
			print "RC mod X != 0"		
		elif (min(R,C) < min_X[X]):
			winner = "RICHARD"
			print "min RC <= min max-aus"
		elif (min(R,C) > min_X[X]):
			winner = "GABRIEL"
			print "max-aus to small"
		elif (min(R,C) == 1):
			print "min_RC = 1"
			winner = "GABRIEL"
		else:
			print "Calculate rows:"
			free_rows = max(R,C)-min(max_X[X],min_X[X])
			print free_rows

			for f in range(0,free_rows):
				f1 = f
				f2 = free_rows-f1
				if ( R*C == f1*min(R,C) + min_X[X]*max_X[X] + f2*min(R,C)):
					print "solution found"
					winner = "GABRIEL"
			print winner
		

		
		line = "Case #"+str(i+1)+": "+winner
		print line
		print " "
		outputfile.write(line+"\n")				
					