#!/usr/bin/env python
import sys

def main():
	[L, D, N] = [int(n) for n in sys.stdin.readline().strip().split()]

	words = []
	for i in range(D):
		words.append(sys.stdin.readline().strip())

	for i in range(N):
		test = sys.stdin.readline().strip()
		print "Case #%d: %d" % (i+1, countMatches(words, test))

def countMatches(dictionary, pattern):
	count = 0
	groups = split(pattern)
	for word in dictionary:
		if matches(word, groups):
			count += 1
	
	return count
	
def matches(word, groups):
	assert(len(groups) == len(word))
	for letter, group in zip(word, groups):
		if not letter in group:
			return False
	return True

def split(pattern):
	groups = []
	group = ''
	inGroup = False
	for letter in pattern:
		if letter == '(':
			inGroup = True
		elif letter == ')':
			inGroup = False
		else:
			group += letter
		
		if not inGroup:
			groups.append(group)
			group = ''
	
	return groups

main()

