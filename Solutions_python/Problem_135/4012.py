# -*- coding: utf-8 -*-

T = int(input())

for i in range(T):
	possible = [ [], [] ]
	result = []
	for j in range(2):
		answer = int(input()) - 1
		cards = [ [], [], [], [] ]
		for k in range(4):
			cards[k] = list(map(int, input().split()))
		possible[j] = cards[answer]

	for n in possible[0]:
		if n in possible[1]:
			result.append(n)

	if result == []:
		print('Case #%d: Volunteer cheated!' % (i+1))
	elif len(result) > 1:
		print('Case #%d: Bad magician!' % (i+1))
	else:
		print('Case #%d: %d' % (i+1, result[0]))

