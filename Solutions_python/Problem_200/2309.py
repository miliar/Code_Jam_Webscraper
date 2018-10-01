#encoding=utf8
filename = "A-large.in"
raw_data = ''
with open(filename, 'r') as f:
	raw_data = f.read().split('\n')

test_count = int(raw_data.pop(0))
for test in range(test_count):
	question = int(raw_data.pop(0))

	qStr = str(question)
	end = len(qStr) - 1
	isPass = True
	for c in range(end):
		if qStr[c] > qStr[c+1]:
			isPass = False

	if isPass == True:
		print "Case #%d:"%(test+1),question
		continue
	
	qStr = str(question)

	while isPass == False:
		isStopLoop = True
		isStarReduce = False
		qStr = str(question)
		end = len(qStr) - 1
		for count in range(end):
			if qStr[count] > qStr[count+1]:
				isStarReduce = True
				qStr = qStr[:count+1] + '0'*(len(qStr) - count -1)
				break

		question = int(qStr) - 1
		qStr = str(question)
		end = len(qStr) - 1
		isPass = True
		for c in range(end):
			if qStr[c] > qStr[c+1]:
				isPass = False

	print "Case #%d:"%(test+1),question