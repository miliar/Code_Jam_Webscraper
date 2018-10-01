#! /usr/bin/env python3
num_tests = int(input())

def read_arrangement():
	ret = []
	for i in range(4):
		ret.append( [int(tok) for tok in input().split(' ')])
	return ret

def solve_test(i):
	first_ans = int(input())
	first = read_arrangement()[first_ans-1]
	second_ans = int(input())
	second = read_arrangement()[second_ans-1]
	possibles = list(set(first) & set(second))
	if (len(possibles) == 1):
		print("Case #{0}: {1}".format(i, possibles[0]))
	elif (len(possibles) > 1):
		print("Case #{0}: Bad magician!".format(i))
	else:
		print("Case #{0}: Volunteer cheated!".format(i))
	
for i in range(1, num_tests+1):
	solve_test(i)
