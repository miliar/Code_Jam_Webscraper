import sys, math

N = int(sys.stdin.readline())

def square(num):
	root = math.sqrt(num)
	if root%1 == 0 and is_palindrome(int(root)):
		return True
	else:
		return False

def is_palindrome(num):
	strNum = str(num)
	if len(strNum) == 3:
		if strNum[0] == strNum[2]:
			return True
	elif len(strNum) == 2:
		if strNum[0] == strNum[1]:
			return True
	elif len(strNum) == 1:
		return True
	else:
		return False

for x in range(1,N+1):
	params = sys.stdin.readline().split()
	A = int(params[0])
	B = int(params[1])

	count = 0

	for y in range(B,A-1,-1):
		if is_palindrome(y) and square(y):
			count += 1

	sys.stdout.write("Case #%d: %d\n" %(x, count))
