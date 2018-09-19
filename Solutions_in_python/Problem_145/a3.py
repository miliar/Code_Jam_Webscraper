#!/usr/bin/python
import fileinput


def log(x):
	if 0:
		print x

def is_power2(num):
	return num != 0 and ((num & (num - 1)) == 0)
	
n = -1
for line in fileinput.input():
	line = line.replace("\n","")
	if n == -1:
		testcases = int(line)
		log("There are " + str(testcases) + " Testcases")	
		n = 0
		continue	
	else:
		n = n + 1
		
	ar = line.split("/")
	#print ar
	p = int(ar[0])
	q = int(ar[1])
	done = 0
	count = 0
	geteilt = q
	if float(p) / float(geteilt) >= 1:
		done = 1	
		count = 1

	while(not done):
		#print "getilt: " + str(geteilt)


		#print "if: " + str(geteilt % 2)
		if geteilt % 2 == 0:
			count = count +1
			geteilt = geteilt / 2
			if float(p) / float(geteilt) >= 1:
				#print geteilt
				if (is_power2(geteilt)):
					#print "ja"
					done = 1
				else:
					if geteilt == p:
						done = 1
					else:
						done = 2	
				
	
		else:
			#print "getilt n: " + str(geteilt) 
			if geteilt == 1:
				done = 1
			else:
				done = 2
		

	if q == 1 and p == 1:
		print "Case #"+str(n)+": "+str(0)
	else:
		if done == 2:
			print "Case #"+str(n)+": impossible" 
		else:
			print "Case #"+str(n)+": "+str(count)
			
