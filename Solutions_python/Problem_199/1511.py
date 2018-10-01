def trim_case(case):
	while True:
		if case and case[0] == 1:
			case = case[1:]
		else:
			break

	while True:
		if case and case[-1] == 1:
			case = case[:-1]
		else:
			break

	return case


def best_flip(case, flipper_size):
	left_gain = 0
	for i in xrange(flipper_size):
		if case and case[i] == 0:
			left_gain += 1
		else:
			break

	right_gain = 0
	for i in xrange(flipper_size):
		if case and case[-(i+1)] == 0:
			right_gain += 1
		else:
			break

	if left_gain >= right_gain:
		return 'left'
	else:
		return 'right'

def flip_left(case, flipper_size):
	case[0:flipper_size] = map(lambda x: int(not bool(x)), case[0:flipper_size])
	return case


def flip_right(case, flipper_size):
	case[-flipper_size:] = map(lambda x: int(not bool(x)), case[-flipper_size:])
	return case


def main():
	n_cases = int(raw_input())
	for i in xrange(n_cases):
		flips = 0
		case, flipper_size = raw_input().split()
		case = map(lambda x: int(x == '+'), case)
		flipper_size  = int(flipper_size)

		case = trim_case(case)

		while len(case) >= flipper_size:
			flip_side = best_flip(case, flipper_size)
			if flip_side == 'left':
				case = flip_left(case, flipper_size)
			else:
				case = flip_right(case, flipper_size)
			flips += 1
			case = trim_case(case)

		if case:
			print "Case #%d: IMPOSSIBLE" % (i + 1)
		else:
			print "Case #%d: %d" % (i + 1, flips)



if __name__ == '__main__':
	main()
