#!/usr/bin/env python

import sys

def processFile(fileName):
	cases = []
	with open(fileName) as f:
		line = f.readline()
		line = f.readline()
		line = f.readline()
		while (line):
			case = [int(n) for n in line.split()]
			cases.append(case)
			line = f.readline()
			line = f.readline()
	return cases


def findMinStepsRecursivly(pancakes, delimeter, amount, currentRes):
	if amount > 8:
		return currentRes
	amount += 1
	result = list(pancakes)
	maxElement = max(pancakes)
	newElement = maxElement / delimeter
	newElement2 = maxElement - newElement
	result.remove(maxElement)
	result.append(newElement)
	result.append(newElement2)

	if max(result) + amount < currentRes:
		currentRes = max(result) + amount

	res1 = findMinStepsRecursivly(result, 2, amount, currentRes)
	res2 = findMinStepsRecursivly(result, 3, amount, currentRes)
	return min(res1, res2)

def findMinSteps(pancakes, amount):
	res1 = findMinStepsRecursivly(pancakes, 2, amount, max(pancakes))
	res2 = findMinStepsRecursivly(pancakes, 3, amount, max(pancakes))
	return min(res1, res2)

def main():
	fileName = sys.argv[1]
	cases = processFile(fileName)
	#print(cases)

	for i in range(0, len(cases)):
		case = cases[i]
		result = findMinSteps(list(case), 0)

		print("Case #%s: %s" % (i+1, result))

if __name__=='__main__':
	main()
