
pas = raw_input()
for i in range(int(pas)):
	arr = []
	real = []
	result = -1
	max = 1
	top = 100
	#Rows
	args = raw_input()
	args = args.split(' ')
	rows = int(args[0])
	columns = int(args[1])
	for a in range(rows):
		vas = raw_input()
		vas = vas.split(' ')
		real.append([top for x in range(columns)])
		arr.append(vas)
		
		for item in vas:
			if item > max:
				max = item
		
	
	for a in range(rows):
		arr[a] = [int(s) for s in arr[a]]
		
	isDone = False
	row = 0
	current = int(max)
	isReverse = False
	column = 0
	while not isDone:
		# not isReverse
		if len(list(set(arr[row]))) < 2:
			max = list(set(arr[row]))[0]
		newList = [1 for e in list(set(arr[row])) if e >= current]
		if len(newList) < 2 and current >= max:
			if not isReverse:
				real[row] = [current for x in range(columns)]
			elif isReverse:
				real[row] = [current for x in range(rows)]
		
		row += 1
		column += 1

		if row == rows and not isReverse:
			isReverse = True
			arr = zip(*arr)
			real = zip(*real)
			row = 0
			column = 0
		elif column == columns and isReverse:
			current -= 1
			isReverse = False
			arr = zip(*arr)
			real = zip(*real)
			column = 0
			row = 0
		
		if current == 0:
			isDone = True
			
	#Compare
	isItOk = True
	for v in range(rows):
		for w in range(columns):
			if arr[v][w] != real[v][w]:
				isItOk = False
				break;
		
	if isItOk == True:
		retStr = 'YES'
	else:
		retStr = 'NO'
	print 'Case #' + str(i+1) + ': ' + retStr