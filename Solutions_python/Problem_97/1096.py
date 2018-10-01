def indexer(plate, limit, threshold, index):
	if len(plate) >= limit:
		index.append(plate)
		return
	for i in range(threshold,10):
		print plate + str(i)
		indexer(plate + str(i), limit, i, index)

def valid_cycles(strnum, b, a):
	allCycles = [strnum[i:]+strnum[0:i] for i in range(len(strnum)) if strnum[i] != '0']
	x = list(set([elem for elem in allCycles if int(elem) <= b and int(elem) >= a]))
	return (len(x)*(len(x)-1))/2

def lowest_form(strnum):
	allCycles = [int(strnum[i:]+strnum[0:i]) for i in range(len(strnum)) if strnum != 0]
	return str(min(allCycles))

def handle(testcase):
	testcase = testcase.split()
	a, b = int(testcase[0]), int(testcase[1])
	counter = str(a)
	result = 0
	handledNumbers = set([])
	while(int(counter) <= int(b)):
		sortedType = lowest_form(counter)
		if ''.join(sortedType) in handledNumbers:
			counter = str(int(counter) + 1)
			continue
		else:
			handledNumbers.add(''.join(sortedType))
		temp = valid_cycles(counter, b, a)
		result += temp
		counter = str(int(counter) + 1)
	print result
	return result
		
f = open('sample.txt', 'r')
fout = open('output.txt', 'w')
fContent = f.read().split('\n')
T = int(fContent[0])
for i in range(T):
	fout.write('Case #'+ str(i+1) + ': ' + str(handle(fContent[i+1])) + '\n')
f.close()
fout.close()