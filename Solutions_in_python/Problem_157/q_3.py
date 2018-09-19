# ___ ______________________________________________ ___ #
#|_/*|                                              |*\_|#
#|_/*|    Google Code Jam - "Hello World"           |*\_|#
#|_/*|    10.04.2015 - the end                      |*\_|#
#|_/*|    Qualification                             |*\_|#
#|_/*|______________________________________________|*\_|#
#|                                                      |#
#|        Denis Werner - denis@nobbd.de                 |#
#|______________________________________________________|#
#                                                        #


filename = "C-large.in"
filename = "C-small-attempt2.in"
#filename = "C-small.in"

lines = ()
with open(filename) as file:
	lines = file.read().splitlines()

number_of_sets = int(lines[0])

with open(filename+".solved","w") as outputfile:
	for i in range(0,number_of_sets):


		#credits = int(lines[i*3+1])
		current_line = lines[i*2+1]
		multi = int(current_line[current_line.index(" "):])
		string_part = lines[i*2+2]
		
		replace = {"ii":"-","ij":"k","ik":"-j","ji":"-k","jj":"-","jk":"i","ki":"j","kj":"-i","kk":"-"}

		full_string = string_part*multi
		
		step = 0
		current_p = 0
		minus = 0
		#print full_string
		while (len(full_string) > 1) and step < 3:
			if step == 0:
				if full_string[current_p] == "i" and minus == 0:
					full_string = full_string[1:]
					step = 1
					print "i complete"
				elif (len(full_string) > 1) and ( full_string[current_p]==full_string[current_p+1]):
					full_string = full_string[current_p+2:]
					minus = (minus +1) %2
					#print "same chars => -"
				else: 
					old = full_string[current_p:current_p+2]
					new = replace[old]
					#print "old: " + full_string
					if ("-" in new):
						minus = (minus +1) %2
						new = new[1:]
					full_string = full_string.replace(old,new,1)
				
				#print "minus: "+str(minus)
				#print "new: " + full_string
			elif step == 1:
				if full_string[current_p] == "j" and minus == 0:
					full_string = full_string[1:]
					step = 2
					print "j complete"
				elif (len(full_string) > 1) and ( full_string[current_p]==full_string[current_p+1]):
					full_string = full_string[current_p+2:]
					minus = (minus +1) %2
					#print "same chars => -"
				else: 
					old = full_string[current_p:current_p+2]
					new = replace[old]
					#print "old: " + full_string
					#print new
					if ("-" in new):
						minus = (minus +1) %2
						new = new[1:]
					full_string = full_string.replace(old,new,1)
			elif step == 2:

				if full_string[current_p] == "k" and minus == 0 and len(full_string) == 1:
					full_string = full_string[1:]
					step = 3
					print "k complete"
				elif (len(full_string) > 1) and (full_string[current_p]==full_string[current_p+1]):
					full_string = full_string[current_p+2:]
					minus = (minus +1) %2
					#print "same chars => -"
				else: 
					old = full_string[current_p:current_p+2]
					new = replace[old]
					#print "old: " + full_string
					#print new
					if ("-" in new):
						minus = (minus +1) %2
						new = new[1:]
					full_string = full_string.replace(old,new,1)	
				#print "minus: "+str(minus)
				#print "new: " + full_string

			#print "new: " + full_string[:20]
		if (full_string == "k" and step == 2 and minus == 0) or step == 3:
			line = "Case #"+str(i+1)+": "+"YES"
		else:
			line = "Case #"+str(i+1)+": "+"NO"		
		print full_string
		print "step: " + str(step)
		print "- "+str(minus)


		# we want ijk

		# i: jk 
		# j: ki 
		# k: ij 

		
		print line
		outputfile.write(line+"\n")				
					