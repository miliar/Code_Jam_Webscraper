with open('input') as fin:
	num_cases = int(fin.readline())

	cases = []
	for i in range(num_cases):
		case = []
		for selections in range(2):
			row = int(fin.readline())
			layout = []
			for rows in range(4):
				layout.append(map(int, fin.readline().strip().split()))

			case.append((row, layout))

		cases.append(case)
# Cases:
# [
#   case: [(row, layout), (row, layout)]
#   ...
# ]
#
# Where layout:
# [[1,2,3,4],
#  [5,6,7,8],
#  ...
#  ...]

for index, case in enumerate(cases):
	first_answer = case[0][0]
	first_row = case[0][1][first_answer - 1]

	second_answer = case[1][0]
	second_row = case[1][1][second_answer - 1]

	possiblities = set(first_row) & set(second_row)

	if len(possiblities) == 1:
		result = possiblities.pop()
	elif len(possiblities) == 0:
		result = "Volunteer cheated!"
	else:
		result = "Bad magician!"

	output = "Case #{}: {}".format(index + 1, result)
	print output
