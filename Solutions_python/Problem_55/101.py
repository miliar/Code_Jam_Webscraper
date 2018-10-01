"""
Theme Park
Author: Cai Xiao
Algorithm:
1. simulate queue procedure until cycle appeared 
we calculate the income as cycleIncome in a cycle and how many times a cycle takes as cycleTimes
incomeList = []
visiteList = {}
while true:
	if (visiteList.has_key(g[0].id):
		cycleStart = visitedList[g[0].id]
		cycleEnd = len(incomeList) - 1
		cycleTimes = cycleEnd - cycleStart + 1
		cycleIncome = sum(incomeList[cycleStart] to incomeList[cycleEnd])
		break
	else:
		visitedList[g[0].id] = len(incomeList)
	while len(g) > 0 and leftSeats >= g[0].num:
		inRoller.append(g[0])
		income = income + g[0].num
		g.popleft()
		incomeList.append(income)
	g.extend(inRoller)
	inRoller = []
	runTime = runTime + 1
	if runTime == R:
		break
2.use incomeList to avoid extra computation 
	totalIncome = sum(incomeList[0] to incomeList[runTime-1])
	if runTime == R:
		return totalIncome
	leftRunTime = R - runTime
	totalIncome += cycleIncome * leftRunTime / cycleTimes 
	totalIncome += sum(incomeList[cycleStart] to incomeList[cycleEnd])	
	return 
"""
import sys
from collections import deque
"""
return (runTime, income)
"""
def SimulateRollerRun(R,K,gList):
	visited = {}
	boardList = []
	income = 0
	runTime = 0
	while True:
		leftSeats = K
		while len(gList) > 0 and leftSeats >= gList[0]['num']:
			boardList.append(gList[0])
			income = income + gList[0]['num']
			leftSeats = leftSeats - gList[0]['num']
			gList.popleft()
			visited[gList[0]['id']] = True
		gList.extend(boardList)
		boardList = []
		runTime = runTime + 1
		if (visited.has_key(gList[0]['id']) or runTime == R):
			break
	return (runTime, income)

def Solve(R,K,gList):
	incomeList = []
	visitedList = {}
	boardList = []
	runTime = 0
	def sum(x,y): return x + y
	while True:
		if (visitedList.has_key(gList[0]['id'])):
			cycleStart = visitedList[gList[0]['id']]
			cycleEnd = len(incomeList) - 1
			cycleTimes = cycleEnd - cycleStart + 1
			cycleIncome = reduce(sum, incomeList[cycleStart:cycleEnd+1])
			break
		else:
			visitedList[gList[0]['id']] = len(incomeList)
		leftSeats = K 
		income = 0
		while len(gList) > 0 and leftSeats >= gList[0]['num']:
			boardList.append(gList[0])
			income = income + gList[0]['num']
			leftSeats = leftSeats - gList[0]['num']
			gList.popleft()
		incomeList.append(income)
		gList.extend(boardList)
		boardList = []
		runTime = runTime + 1
		if (runTime == R):
			break
	
	totalIncome = reduce(sum, incomeList)
	if runTime == R:
		return totalIncome
	leftRunTime = R -runTime
	totalIncome = totalIncome + cycleIncome * (leftRunTime / cycleTimes)
	if (leftRunTime % cycleTimes != 0):
		totalIncome = totalIncome + reduce(sum,incomeList[cycleStart:cycleStart+leftRunTime % cycleTimes])
	return totalIncome
	
if __name__ == "__main__":
	input_file = open(sys.argv[1])
	output_file = open(sys.argv[2],'w')
	t = int(input_file.readline())
	for i in range(t):
		ss = input_file.readline().split(' ')
		R = int(ss[0])
		K = int(ss[1])
		ss = input_file.readline().split(' ')
		id = 0
		gList = deque([]) 
		for x in ss:
			gList.append({'id':id,'num':int(x)})
			id = id + 1
		res = Solve(R,K,gList)
		output_file.write('Case #' + str(i+1) + ': ' + str(res) + '\n')
	
	input_file.close()
	output_file.close()

	
		
