from collections import deque

file = open("tidynumbers.in", "r")
numCases = int(file.readline())

# 132
# 129

def forward(N):
	last = 0
	counter = 0
	for n in N:
		num = int(n)
		if num >= last:
			last = num
			counter += 1
		else:
			return counter - 1

def updated(N, i):
	listN = list(N)
	if listN[i] == '1':
		for ii in range(1, len(listN)):
			listN[ii] = '9'
		return ''.join(listN[1:])
	else:
		listN[i] = str(int(listN[i]) - 1)
		for ii in range(i+1, len(listN)):
			listN[ii] = '9'
		return ''.join(listN)


def run(N):
	#print(N)
	i = 0
	while not i == None:
		i = forward(N)
		if not i == None:
			N = updated(N, i)

	return N



for caseId in range(numCases):
	line = file.readline()
	last = run(line[:-1])
	if not last == None:
		print('Case #%d: %s' % (caseId + 1, last))

