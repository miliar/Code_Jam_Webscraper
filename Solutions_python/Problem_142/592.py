#!/usr/bin/env python


def prepareString(s):
	array = list(s)
	letters = []
	counts = []
	prev_letter = None
	cur_count = 0

	for cur_letter in array:
		if prev_letter is not None:
			if cur_letter == prev_letter:
				cur_count += 1
			else:
				counts.append(cur_count)
				prev_letter = cur_letter
				letters.append(cur_letter)
				cur_count = 1
		else:
			prev_letter = cur_letter
			cur_count = 1
			letters.append(cur_letter)

	counts.append(cur_count)
	return letters, counts


def compare(list1, list2):
	if len(list1) != len(list2):
		return False
	for i in range(len(list1)):
		if list1[i] != list2[i]:
			return False
	return True


for t in range(int(raw_input())):
	n = int(raw_input())
	letters = []
	counts = []
	for i in range(n):
		l, c = prepareString(raw_input())
		letters.append(l)
		counts.append(c)

	isWon = False
	for i in range(n - 1):
		if not compare(letters[i], letters[i+1]):
			isWon = True
			break
	if isWon:
		print 'Case #{0}: Fegla Won'.format(t + 1)
	else:
		answer = 0
		for i in range(len(letters[0])):
			answer += abs(counts[0][i] - counts[1][i])
		print 'Case #{0}: {1}'.format(t + 1, answer)
