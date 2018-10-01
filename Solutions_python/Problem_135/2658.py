#!/usr/bin/python

import sys

def do_magic_trick(case, first_answer, second_answer, cards, cards2):
	first_attempt = cards[first_answer - 1]
	second_attempt = cards2[second_answer - 1]

	first_attempts = first_attempt.split()
	second_attempts = second_attempt.split()

	intersection = list(set(first_attempts) & set(second_attempts))

	if len(intersection) == 1:
		answer = intersection[0]
	else:
		answer = 'Bad magician!' if len(intersection) > 1 else 'Volunteer cheated!'

	print 'Case #{0}: {1}'.format(case + 1, answer)


def main():
	filename = sys.argv[1:]
	f = open(filename[0])

	test_case = int(f.readline())

	for case in range(test_case):
		first_answer = f.readline()

		cards = []
		for cards_row in range(4):
			cards.append(f.readline())

		second_answer = f.readline()

		cards2 = []
		for cards_row in range(4):
			cards2.append(f.readline())

		do_magic_trick(int(case), int(first_answer), int(second_answer), cards, cards2)

if __name__ == '__main__':
	main()