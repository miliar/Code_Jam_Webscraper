
import sys
sys.setrecursionlimit(10000)

#open file
file = open('./input.in', 'r')

def solve(c, f, x, f0, totalTime):

	if (totalTime + x/f0)<(totalTime + c/f0 + x/(f0+f)):
		return (totalTime+x/f0)
	else:
		#create farm
		return solve(c, f, x, f+f0, totalTime+(c/f0))


numcases = int(file.readline())
for casenum in range(1,numcases+1):

	#read line and save input value
	input = file.readline().split()
	c = float(input[0])
	f = float(input[1])
	x = float(input[2])

  	print 'Case #' + repr(casenum) + ': ' + '%.7f'%solve(c, f, x, 2.00, 0.0)