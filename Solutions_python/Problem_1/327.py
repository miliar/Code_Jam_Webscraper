#! /usr/bin/python

inpfile = open('small2.in', 'r')

inpCount = int (inpfile.readline())
ind = 0
case = 0
while ind < inpCount:
	engineCount = int (inpfile.readline())
	a = 0
	engineNames = []
	while a < engineCount:
		temp1 = inpfile.readline()
		engineNames.append (temp1.strip("\n"))
 		a = a + 1
	#print engineNames

	queryCount = int (inpfile.readline())
	b = 0
	queryNames = []
	while b < queryCount:
		temp2 = inpfile.readline()
		queryNames.append (temp2.strip("\n"))
		b = b + 1
	#print queryNames

	d = 0
	flip = 0
	temp3 = []
	while d < queryCount:
		if queryNames[d] not in temp3:
			temp3.append (queryNames[d])
			if len(temp3) == engineCount:
				d = d - 1
				temp3 = []
				flip = flip + 1
		d = d + 1		
	
	case = ind + 1	
	print "Case #%d: %d" % (case,flip)
 	ind = ind + 1
