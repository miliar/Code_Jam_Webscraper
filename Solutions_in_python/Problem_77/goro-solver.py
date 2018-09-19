def solveTask(number, line):
	arr = line.strip().split()
	arr = map (lambda x: int(x), arr)
	sortedArray = line.strip().split()
	sortedArray = map (lambda x: int(x), sortedArray)
	sortedArray.sort()
	zipped = zip(arr, sortedArray)
	print zipped
	res = len(filter(lambda (x,y): x != y, zipped))
	return "Case #{0}: {1}.000000\n".format(number,res)

def solveFile(fileName):
	f = open(fileName)
	fr = open("d:\\res.txt","w")
	lines = f.readlines()
	tasks = lines[1:]
	taski = map(lambda i: tasks[i],filter(lambda i: i%2 == 1,range(len(tasks))))
	readyTasks = zip(range(len(taski)),taski)
	map(lambda(x,y): fr.write(solveTask(x+1, y)), readyTasks)
	f.close()
	fr.close()
	return
