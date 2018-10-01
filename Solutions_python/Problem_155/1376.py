#!/usr/bin/env python3

from sys import *

def solve(line):
	line = line.strip("\n")
	people = list(line.split(" ")[1])
	standing = 0
	friends = 0
	for i, x in enumerate(people):
		if(i <= standing):
			standing += int(x)
		else:
			diff = i - standing
			friends += diff
			standing += diff
			standing += int(x)
	return str(friends)

def main():
	counter = int(stdin.readline())
	for x in range(counter):
		output = solve(stdin.readline())
		print('Case #' + str(x + 1) + ': ' + output)

if __name__ == "__main__":
	main()
