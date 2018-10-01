

def parseCase():
	digits = [int(c) for c in input()]
	return digits


def solveCase(case):
	sol = ltidy(case)
	return int(''.join([str(d) for d in sol]))


def ltidy(digits):
	for i in range(len(digits) - 1):
		if digits[i + 1] < digits[i]:
			digits[i] = digits[i] - 1
			return ltidy(digits[: i + 1]) + ([9] * len(digits[i + 1 :]))
	return digits


if __name__ == '__main__':
	t = int(input())
	for i in range(1, t + 1):
		case = parseCase()
		sol = solveCase(case)
		print("Case #{0}: {1}".format(i, sol))
