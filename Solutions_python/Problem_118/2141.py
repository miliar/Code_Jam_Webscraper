import sys
from math import sqrt

def palindrome(num):
	num = str(int(num))
	return num == num[::-1]

def get_sqrt(n):
	sq = int(sqrt(n) + 0.5)
	if (sq**2) == int(n):
		return sq
	return -1

def solve(line):
	line = line.split()
	low = int(line[0])
	high = int(line[1])
	count = 0
	for i in range(low, high+1):
		s = get_sqrt(i)
		if s > 0 and palindrome(s) and palindrome(i):
			count += 1
	return count

def main():
	lines = sys.stdin.readlines()
	N = int(lines[0])
	for i in range(1,N+1):
		print "Case #" + str(i) + ": " + str(solve(lines[i]))
	#print lines

main()