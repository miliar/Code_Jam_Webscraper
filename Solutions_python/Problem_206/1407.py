
def main():
	with open('A-large.in', 'r') as f:
		cases = f.readlines()

	answers = []
	speeds = []
	total_cases = cases[:1]
	case_array = []
	# for n in range(total_cases):
	num_horses = 0
	for i, case in enumerate(cases[1:]):
		case_split = case.split()
		if num_horses == 0:
			max_speeds = []
			destination = int(case_split[0])
			num_horses = int(case_split[1])
		else:
			K = int(case_split[0])
			S = int(case_split[1])
			hours = (destination - K)/S
			max_speed = destination/hours
			max_speeds.append(max_speed)
			num_horses = num_horses - 1
		if num_horses == 0:
			speed = min(max_speeds)
			speeds.append(speed)

	for n, x in enumerate(speeds):
		string = 'Case #' + str(n+1) + ': ' + str(x) + '\n'
		answers.append(string)

	print(answers)
	return answers


if __name__ == "__main__":
	answers = main()

	with open('result3.txt', 'w')as k:
		for answer in answers:
			for a in answer:
				k.write(a)