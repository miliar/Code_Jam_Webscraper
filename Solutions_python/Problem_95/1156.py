from sys import stdin

f = open('output.out', 'w')
for i in range(0, int(stdin.readline())):
	lineArray = stdin.readline().split()[1:]
	#print lineArray
	o = []
	b = []
	sequence = []
	for j in range(0, len(lineArray), 2):
		sequence.append(lineArray[j])
		if lineArray[j] == 'O':
			o.append(int(lineArray[j+1]))
		else:
			b.append(int(lineArray[j+1]))
	
	#print sequence
	#print o,b
	
	oPos = 1
	bPos = 1
	steps = 0
	
	oI = 0
	bI = 0
	orI = 0
	incrementO = 0
	incrementB = 0
	
	while (orI < len(sequence)):
		# orange side
		if oI < len(o):
			if o[oI] > oPos:
				oPos += 1
			elif o[oI] < oPos:
				oPos -= 1
			elif sequence[orI] == 'O':
				# if step is current then button push
				incrementO = 1
		# blue side			
		if bI < len(b):		
			if b[bI] > bPos:
				bPos += 1
			elif b[bI] < bPos:
				bPos -= 1
			elif sequence[orI] == 'B':
				# if step is current then button push			
				incrementB = 1
				
		#print oPos, bPos		
		steps += 1
		
		if incrementO:
			oI += 1
			orI += 1
			incrementO = 0
		elif incrementB:
			bI += 1
			orI += 1
			incrementB = 0
	#print
	f.write('Case #'+str(i+1)+': ' + str(steps) + '\n')
		
f.close()
