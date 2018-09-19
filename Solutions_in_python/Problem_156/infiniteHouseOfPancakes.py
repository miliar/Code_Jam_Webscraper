#InfiniteHouseOfPancakes

def pancakes(case, d, p):
	cakes_s = p.split(' ')
	cakes = makeInt(cakes_s)
	minutes = 1000
	#my_cakes = makeInt(cakes_s)

	M = max(cakes)
	#print "max", M
	#print cakes	
	
	if M <= 2:
		minutes = M
		
	else: 	
		for i in range(2, M+1):
			my_cakes = makeInt(cakes_s)
			mins = 0
			#print "i", i
			for j in range(len(my_cakes)):
				div = my_cakes[j]/i
				mod = my_cakes[j]%i
				#print "div plate", j, div
				if div == 0: 
					continue
				else:
					my_cakes[j] = mod
					#for k in range(div):
						#my_cakes.append(i)
					
					if mod == 0:
						mins += div - 1
					else:
						mins += div
				#print my_cakes
			mins += i
		
			if 0 < mins < minutes:
				minutes = mins
				#print "min mins", minutes	
			
	print "Case #" + str(case) + ": " + str(minutes)
			
def makeInt(c):
	d = []
	for i in c:
		d.append(int(i))
	return d

inp = raw_input()
T = int(inp)

for i in range(T):
	new_inp = raw_input()
	pans = raw_input()
	pancakes(i+1, int(new_inp), pans)
			
#pancakes('1', '1', '3')
#pancakes('1', '4', '1 2 1 2')
#pancakes('1', '1', '4')
