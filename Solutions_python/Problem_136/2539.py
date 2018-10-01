#!/usr/bin/python
import fileinput


def log(x):
	if 0:
		print x


n = -1
for line in fileinput.input():
	if n == -1:
		testcases = int(line)
		log("There are " + str(testcases) + " Testcases")	
		n = 0
		continue	
	else:
		n = n + 1
		
		
	log("=======================================================")
	log("Doing Testcase " + str(n) + ":")
	
	# read the rows
	c = float(line.split()[0])
	f = float(line.split()[1])
	x = float(line.split()[2])
	log("C: "+str(c)+" F: " + str(f) + " X: " + str(x))
	
	
	m = list()	# current cps
	g = list()  # overall duration
	d = list()  # distance in s between purchases
	t = list()  # timestampe of purchases
	

	i = 0
	# current cps
	m.append(2)
	log ("m_"+str(i)+": " + str(m[i]))
	
	# calc distance to next buy
	d.append(c/m[i])
	log ("d_"+str(i)+": " + str(d[i]))
	
	# calc distance from beginning
	t.append(d[i])
	log ("t_"+str(i)+": " + str(t[i]))
	
	# calc overall duration with current rate till getting to X
	g.append(x/m[i])
	log ("g_"+str(i)+": " + str(g[i]))	
	
	g_min = g[0]

	done = 0

	while(not done):
		i = i + 1
		log("---")
		log("Doing step " + str(i) + ":")
		
		# current cps with new farm
		m.append(m[i-1]+f)
		log ("m_"+str(i)+": " + str(m[i]))
		
		# calc distance to next buy
		d.append(c/m[i])
		log ("d_"+str(i)+": " + str(d[i]))
		
		# calc distance from beginning
		t.append(t[i-1] + d[i])
		log ("t_"+str(i)+": " + str(t[i]))			
		
		# calc overall duration with current rate
		g.append(t[i-1] + x/m[i])
		log ("g_"+str(i)+": " + str(g[i]))
		
		# check if this is fastest way
		if g[i] < g_min:
			done = 0 # do another round
			g_min = g[i]
		else: # it takes longer with this factory than the perviouse iteration
			done = 1
			print "Case #"+str(n)+": " +str(g[i-1])
			

		
		

	
	
