def calculateTime(c,f,x,cap):
	print 'calculating time for cap: '+str(cap)
	farms = 0
	sum = 0
	while True:
		if farms >= cap:
			# exit cookie factory purchase loop at specified cap
			break
		
		aggregate = farms*f + 2.0 
		#print 'buying farm #'+str(farms+1)+' at aggregate '+str(aggregate)
		seconds = c/float(aggregate)
		sum += seconds
		
		farms += 1
	
	aggregate = f*farms + 2.0
	#print 'now collecting cookies at aggregate '+str(aggregate)

	sum += x/float(aggregate)
	return sum


def compareStrategies(c,f,x):
	# cycle through all possible strategies to find where the optimal strategy is
	farms = 0
	store = []

	while True:
		try:
			previous = store[-1]
			store.append(calculateTime(c,f,x,farms))
			current = store[-1]
			if current > previous:
				# minimal time is right before values increase again
				return previous
		except IndexError:
			# first run has empty store, thus indexerror
			store.append(calculateTime(c,f,x,farms))

		farms += 1


# open input, calculate time, write out
wf = open('output.txt','w')
f = open('input.txt','r')
for i,line in enumerate(f):
	line.strip('\n')
	if i == 0:
		cases = int(line)
	else:
		# get values from line
		C,F,X = [float(x) for x in line.split(' ')]
		# find optimal time for values
		time = compareStrategies(C,F,X)
		wf.write("Case #"+str(i)+": "+str(round(time,7))+'\n')
wf.close


