def newpieces(n):
	if n % 2 == 1:
		a = (n - 1) // 2
		b = a
	else:
		a = n // 2
		b = a - 1
	return [a,b]

def addtolist(l,n,instances):
	#print('adding ' + str(instances) + ' instances of ' + str(n) + ' to ' + str(l))
	for i in range(len(l)):
		if l[i][0] == n:
			#print('I got ' + str(l[:i] + [[l[i][0],l[i][1] + instances]] + l[i:]))
			return l[:i] + [[l[i][0],l[i][1] + instances]] + l[(i+1):]
	#print('I got ' + str(l + [[n,instances]]))		
	return l + [[n,instances]]
	
def f(n,k):
	slist = [['',''],[n,1]]
	count = 0
	while True:
		nextbatch = slist.pop(1)
		count += nextbatch[1]
		np = newpieces(nextbatch[0])
		if count >= k:
			return str(np[0]) + ' ' + str(np[1])
		else:
			slist = addtolist(slist,np[0],nextbatch[1])
			slist = addtolist(slist,np[1],nextbatch[1])
		
import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		pair = [int(x) for x in inputLines.pop(0).rstrip().split()]
		fileOUT.write('Case #' + str(num+1) + ': ' + f(pair[0],pair[1]) + '\n')
		print(num) # This is just to track progress.