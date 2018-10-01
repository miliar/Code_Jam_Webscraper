
def run():
	testCaseCount = eval(input())

	for i in range(testCaseCount):
		C,F,X = [eval(s) for s in input().split(' ')]
		P = 2
		totalTime = 0

		while X/P > (C/P + X/(P+F)):
			totalTime += C/P
			P += F

		totalTime += X/P
		print("Case #{:d}: {:.7f}".format(i+1, totalTime))


if __name__ == '__main__':
	run()