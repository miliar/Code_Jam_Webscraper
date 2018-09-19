import sys

def getProfit(runs, size, groups):
	profit = 0
	for i in range(runs):
		p = 0
		g = 0
		#print groups
		while g < len(groups) and p + groups[0] <= size:
			p = p + groups[0]
			g = g + 1
			groups = groups[1:] + groups[0:1]
		#print p
		profit = profit + p
	return profit

input = open(sys.argv[1])
output = open(sys.argv[2], 'w')

C = int(input.readline())

for i in range(C):
	line = input.readline().split()
	R = int(line[0])
	k = int(line[1])
	N = int(line[2])
	groups = map(lambda n: int(n), input.readline().split())
	profit = getProfit(R, k, groups)
	output.write('Case #'+str(i+1)+': '+str(profit)+'\n')

input.close()
output.close()