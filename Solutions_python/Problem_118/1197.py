import math

def main():
	with open('C-small-attempt0.in') as f:
		ntests = int(f.readline())
		lines = f.readlines()
		i = 1
		for line in lines:
			lo, hi = line[:-1].split(' ')
			n = treat_case(lo, hi)
			print "Case #%d: %d" % (i, n)
			i += 1

def treat_case(lo, hi):
	n = 0
	for i in range(int(lo), int(hi)+1):
		if ispalindrome(i):
			root = math.sqrt(i)
			if (root%1 == 0) and ispalindrome(int(root)):
				n+=1
	return n

def ispalindrome(n):
	return str(n) == str(n)[::-1]


main()