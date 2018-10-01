#!/usr/bin/env python

#open input file
f = open("small_A.in", "r")

#reading the total number of cases
number = f.readline()

#prepare variables for storing
case = 0 # number of cases read; always < number
string = "" # string to be outputted
googlerese = {"a":"y", "b":"h", "c":"e", "d":"s", "e":"o", "f":"c", "g":"v", "h":"x", "i":"d", "j":"u", "k":"i", "l":"g", "m":"l", "n":"b", "o":"k", "p":"r", "q":"z", "r":"t", "s":"n", "t":"w", "u":"j", "v":"p", "w":"f", "x":"m", "y":"a", "z":"q"} # replacement dictionary

#process file
chars = googlerese.values()
for line in f:
	length = len(line)
	string = ""
	#run through each line and decode Googlerese to English
	for index in range(0,length):
		if line[index] in chars:
			string = string + googlerese[line[index]]
		else:
			string = string + " "
	
	case = case + 1
	print "Case #"+str(case)+": "+string

	if case+1 == number:
		break

f.closed
