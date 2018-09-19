
def isPalindrome(number) :
	s = str(number)
	l = len(s)
	for i in range(l/2) :
		if s[i] != s[l - i - 1] :
			return False
	return True

def isFaSRoot(number) :
	if isPalindrome(number) :
		return isPalindrome(number * number)
	return False

def countFaS(start, end) :
	rootS = int(math.ceil(math.sqrt(start)))
	rootE = int(math.floor(math.sqrt(end)))
	n = rootS
	count = 0
	while (n <= rootE) :
		if isFaSRoot(n) :
			count += 1
		n += 1
	return count

# it starts here
import sys
import math

l = sys.stdin.readline()
count = int(l)

results = []
for i in range(count) :
	a,b = sys.stdin.readline().split()
	start = int(a)
	end = int(b)

	n = countFaS(start, end)
	results.append(n)

# print results
for i in range(count):
	msg = str(results[i])
	print 'Case #' + str(i+1) + ": " + msg
