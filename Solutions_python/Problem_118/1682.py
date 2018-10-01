import math
import random

def isPreparedNumberFair(number):
	"""
	A prepared number is one with even digits
	"""
	chars = list(number)
	for i in range(len(number)):
		if chars[i] != chars[len(number) - 1 - i]:
			return False
	return True

def prepareNumber(number):
		arr = list(number)
		arr.pop(len(number) / 2)
		return ''.join(arr)

def isNumberFair(number):
	numString = str(number)
	if len(numString) == 1:
		return True
	if len(numString) % 2 == 0:
		#Even number of characters
		return isPreparedNumberFair(numString)
	else:
		#odd number of characters
		#Remove the middle element
		return isPreparedNumberFair(prepareNumber(numString))


def findAllFasLessThan(cap):
	faSNumbers = []
	i = 0
	square = 0
	while square <= cap:
		i += 1
		square = i**2
		if isNumberFair(square) and isNumberFair(i):
			print square
			faSNumbers.append(square)
	return faSNumbers
		
def readInputFile(fileName):
	out = open('ouput.txt', 'w+')
	inp = open(fileName, 'r')
	#first is number of cases
	cases = inp.readline()
	faSNumbers = findAllFasLessThan(10**14)
	for i in range(int(cases)):
		bottomTop = inp.readline()
		print bottomTop
		bottom = int(bottomTop.split()[0])
		top = int(bottomTop.split()[1])
		faSCount = 0
		for num in faSNumbers:
			if num > top:
				break
			if num >= bottom:
				faSCount += 1
		i += 1
		out.write("Case #{0}: {1}\n".format(i, faSCount))


readInputFile('C-large-1.in')
