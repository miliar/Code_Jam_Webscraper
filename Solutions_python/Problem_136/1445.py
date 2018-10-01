import sys
import math
sys.setrecursionlimit(10000) 
T = int(sys.stdin.readline())

def main():
	for case in range(1,T+1):
		global timeNow, initYield, currentNumberFarm, currentCookies
		timeNow = 0
		initYield = 2
		currentNumberFarm = 0
		currentCookies = 0

		res = solve(case)
		sys.stdout.write("Case #{}: {}\n".format(case, res));

def solve(case):
	numbers = map(float, sys.stdin.readline().split())
	priceFarm = numbers[0]
	yieldFarm = numbers[1]
	cookiesGoal = numbers[2]

	if priceFarm > cookiesGoal:
		return  timeToProduce(cookiesGoal, getCurrentYield(yieldFarm))
	else:
		return iterate(priceFarm, yieldFarm, cookiesGoal)


def iterate(priceFarm, yieldFarm, cookiesGoal):
	global timeNow
	timeNow += timeToProduce(priceFarm, getCurrentYield(yieldFarm))

	timeGoalDontBuy = timeToProduce(cookiesGoal-priceFarm, getCurrentYield(yieldFarm))
	timeGoalBuy = timeToProduce(cookiesGoal, getCurrentYield(yieldFarm)+yieldFarm)

	if timeGoalBuy < timeGoalDontBuy:
		buyFarm()
		return iterate(priceFarm, yieldFarm, cookiesGoal)
	else:
		return timeNow + timeGoalDontBuy


def buyFarm():
	global currentNumberFarm
	currentNumberFarm += 1

def timeToProduce(cookies, thisYield):
	return cookies/thisYield

def getCurrentYield(yieldFarm):
	return initYield + currentNumberFarm*yieldFarm


timeNow = 0
initYield = 2
currentNumberFarm = 0
currentCookies = 0

main()


