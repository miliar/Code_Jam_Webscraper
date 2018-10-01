import sys

multi = "Bad magician!"
none = "Volunteer cheated!"

def compareSubtract(x,y):
	return x[0] - y[0]

def getOutputName(inputName):
	print inputName.split('.')[0] + ".out"
	return inputName.split('.')[0] + ".out"

def writeAnswer(case, answer, file):
	print "Case #%(tc)d: %(answer)s" % {'tc': case , 'answer':answer}
	file.write("Case #%(tc)d: %(answer)s" % {'tc': case , 'answer':answer})
	file.write("\n")
def writeAnswers(answers, file):
	for i in range(len(answers)):
		writeAnswer(i+1, answers[i], file)

def doTrial(data):
	#implement trial test case here an return the data in a readable format
	answer = int(data.readline())
	remaining = 4 - answer
	possible = set([])
	while answer > 0:
		possible = set([int(x) for x in data.readline().split(' ')])
		answer -= 1
	while remaining > 0:
		data.readline()
		remaining -= 1
	
	answer = int(data.readline())
	remaining = 4 - answer
	possibleTwo = set([])
	while answer > 0:
		possibleTwo = set([int(x) for x in data.readline().split(' ')])
		answer -= 1
	while remaining > 0:
		data.readline()
		remaining -= 1
		
	ans = possible & possibleTwo
	if len(ans) < 1:
		return none
	elif len(ans) > 1:
		return multi
	else:
		return ans.pop()
	
if len(sys.argv) > 1:
	fin = file(sys.argv[1])
	fout = file(getOutputName(sys.argv[1]),'w')
	count = 0
	
	numTC = int(fin.readline())
	

	ans = []
	for case in range(numTC):
		data = None
		###### Read in data here from fin, and parse answers.
		data = fin
		
		
		##### put into some type of readable format.
		##### process the data
		answer = doTrial(data)
		print answer
		ans.append(answer)
	writeAnswers(ans,fout)
	fin.close()
	fout.flush()
	fout.close()