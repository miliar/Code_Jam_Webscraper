import sys, math

#Write first recursive, greedy solution.
def recurseGreed(currentTime, currentRate, farmprice, farmrate, goal): 
	if goal <= farmprice:
		return currentTime+goal/currentRate
	elif goal/currentRate < (farmprice/currentRate+ goal/(currentRate+farmrate)):
		return currentTime+goal/currentRate
	else:
		return min(currentTime + goal/currentRate, recurseGreed(currentTime+farmprice/currentRate, currentRate+farmrate, farmprice, farmrate, goal))
	
#Closen formula for maximum number of farms that need to be built (as base case for bottom-up DP?)
#Never mind bottom up... At least goal farms added is an upper limit.
def iterate(farmprice, farmrate, goal):
	farms = [(0, goal/2)]
	times = [goal/2]
	rate = 2
	for idx in range(1, int(goal)+2):
		farmtime = farmprice/rate+farms[idx-1][0]
		rate += farmrate
		remaining = goal/rate
		farms.append((farmtime, remaining))
		times.append(farmtime+remaining)
	#What is the complexity of min?
	return min(times)
	
		
		

nrC = int(sys.stdin.readline().strip())
for i in range(1, nrC+1):
	print "Case #"+str(i)+":",
	[farmprice, farmrate, goal] = [float(x) for x in sys.stdin.readline().strip().split()]
	ans = iterate(farmprice, farmrate, goal)
	print "{0:.7f}".format(ans)
