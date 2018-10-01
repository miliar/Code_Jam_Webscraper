import math

def isPalindrome(s):
	return s == s[::-1]

def isFairSquare(x):
	root = math.sqrt(x)
	isSquare = root.is_integer()
	return isSquare and isPalindrome(str(x)) and isPalindrome(str(int(root)))
	
count = int(raw_input())
for case in range(1, count + 1):
	bounds = [int(x) for x in raw_input().split()]
	bounds[1] += 1
	y = range(*bounds)
	fs = [z for z in y if isFairSquare(z)]
	print "Case #" + str(case) + ": " + str(len(fs))