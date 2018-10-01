import math
import sys
def main():
	inputFile = sys.argv[1]
	f = open(inputFile, "r")
	o = open("output.txt", "w")
	numOfTestCases = int(f.readline()[:-1])
	for x in range(numOfTestCases):
		result = 0
		if x == numOfTestCases - 1:
			line = f.readline()
		else:
			line = f.readline()[:-1]
		low = int(line.split(' ')[0])
		high = int(line.split(' ')[1])

		for i in range(low, high + 1):
			# print i
			if isPalindrome(i) and int(math.sqrt(i)) == math.sqrt(i):
				if isPalindrome(int(math.sqrt(i))):
					result = result + 1

		# start = int(math.ceil(math.sqrt(low)))
		# print "interval:" + str(low) + "...." + str(high)
		# while start * start <= high:
		# 	if isPalindrome(start):
		# 		if isPalindrome(start * start):
		# 			print start
		# 			print start * start
		# 			result = result + 1
		# 	start = start + 1
		# if not result == testing(low, high):
		# 	print "Error is at " + str(low) + "  " + str(high)
		# 	print (result, testing(low, high))
		# # print "----------------"
		o.write("Case #" + str(x + 1) + ": " + str(result) + "\n")

def testing(low, high):
	result = 0
	for i in range(low, high + 1):
		# print i
		if isPalindrome(i) and int(math.sqrt(i)) == math.sqrt(i):
			if isPalindrome(math.sqrt(i)):
				print (i, math.sqrt(i))
				result = result + 1
	return result


def isPalindrome(number):
	shortDiv = 10
	longDiv = 10
	if number < 10:
		return True
	while number / longDiv >= 10:
		longDiv = longDiv * 10
	while not number == 0:
		front = number / longDiv
		end = number % shortDiv
		if not front == end:
			return False
		number = (number % longDiv) / 10
		longDiv = longDiv / 100
	return True



if __name__ == "__main__":
    main()