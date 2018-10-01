input = open("A-small-attempt1.in", 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines]

out = open("output.txt", 'w+')

no_of_cases = int(lines[0])
start_line = 1
line_increment = 10
end_line = line_increment + 1

for case_no in xrange(1, no_of_cases + 1):
	case = lines[start_line:end_line]

	first_answer = case[0]
	second_answer = case[5]
	first_arrangement = case[1:5]
	second_arrangement = case[6:]
	print first_answer
	print first_arrangement
	print second_answer
	print second_arrangement

	first_answer_row = first_arrangement[int(first_answer) - 1]
	print first_answer_row
	second_answer_row = second_arrangement[int(second_answer) - 1]
	print second_answer_row

	#print first_answer_row, second_answer_row
	cards = list(set(first_answer_row.split()) & set(second_answer_row.split()))
	if len(cards) == 0:
		cards = "Volunteer cheated!"
	elif len(cards) > 1:
		cards = "Bad magician!"
	else:
		cards = cards[0]

	print str(case_no) + " " + str(cards)
	start_line = end_line
	end_line += line_increment
	out.write("Case #" + str(case_no)  + ": " + cards + '\n')