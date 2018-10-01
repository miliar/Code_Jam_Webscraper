#!/usr/bin/python3
def flip(c):
	return '+' if c is '-' else '-'

t = int(input())

for testcase in range(t): 
	line = input().split()
	s = list(line[0])
	k = int(line[1])

	count = 0
	for c in range(len(s)-k):
		if s[c] == '-':
			count += 1
			for i in range(k):
				s[c+i] = flip(s[c+i])

	if '-' not in s[-k:]:
		print("Case #{}: {}".format(testcase+1, count))
	elif '+' not in s[-k:]:
		print("Case #{}: {}".format(testcase+1, count+1))
	else:
		print("Case #{}: IMPOSSIBLE".format(testcase+1))