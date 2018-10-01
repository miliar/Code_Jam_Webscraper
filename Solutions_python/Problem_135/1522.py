from itertools import islice
import os

abpath = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

ANSWER = "Case #{}: {}"
BAD_MAG = "Case #{}: Bad magician!"
CHEAT = "Case #{}: Volunteer cheated!"


def solve(in_path, out_path):
	case_num = 1
	test_cases = 0

	with open(in_path, "rb") as i, open(out_path, "w+b") as o:
		test_cases = int(i.readline())
		while True:
			case = list(islice(i, 10))
			if not case:
				break
			
			solution = solve_case(
				int(case[0]), [case[1], case[2], case[3], case[4], ],
				int(case[5]), [case[6], case[7], case[8], case[9], ],
				case_num
			)
			o.write(solution)
			if case_num < test_cases:
				o.write("\n")

			case_num += 1


def solve_case(first_row, first_cards, second_row, second_cards, case_num):
	first_poss_cards = map(int, first_cards[first_row - 1].split(' '))
	second_poss_cards = map(int, second_cards[second_row - 1].split(' '))

	all_poss_cards = set(first_poss_cards).intersection(second_poss_cards)

	if len(all_poss_cards) == 0:
		# cheating volunteer
		answer = CHEAT.format(case_num)
	elif len(all_poss_cards) == 1:
		# we've got a card
		answer = ANSWER.format(case_num, int(all_poss_cards.pop()))
	else:
		# bad magician
		answer = BAD_MAG.format(case_num)

	return answer


if __name__ == '__main__':
	solve(abpath("A-small-attempt2.in"), abpath("A-small-attempt2.out"))
