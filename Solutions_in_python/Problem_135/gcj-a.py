#! /bin/env python3
#! -*- coding: utf-8 -*-

ifn = 'A-small-attempt0.in'

def get_chosen_row(input):
	answer = int(input.readline())
	# jump to chosen row
	for _ in range(1, answer):
		input.readline() # skip row
	row = [int(x) for x in input.readline().split(' ')]
	# jump to second chosen row
	for _ in range(answer, 4):
		input.readline() # skip row
	return row

def print_answer(case, diff):
	case_format = 'Case #%d: %s'
	if len(diff) == 0:
		print(case_format % (case, 'Volunteer cheated!'))
	elif len(diff) == 1:
		print(case_format % (case, diff.pop()))
	else:
		print(case_format % (case, 'Bad magician!'))

with open(ifn, 'r') as input:
	T = int(input.readline())
	for case in range(0, T):
		row1 = get_chosen_row(input)
		row2 = get_chosen_row(input)
		diff = set(row1).intersection(set(row2))
		print_answer(case+1, diff)