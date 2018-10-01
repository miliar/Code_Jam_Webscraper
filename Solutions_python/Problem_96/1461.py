dances = open("B-large.in", 'r')
dances.readline()
answer = open("dancers-big.out", 'w')
surp_matters = [2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 24, 26, 27]
max_dict = {0: 0, 1: 1, 2: 4, 3: 7, 4: 10, 5: 13, 6: 16, 7: 19, 8: 22, 9: 25, 10: 28}
max_surp_dict =  {0: 0, 1: 1, 2: 2, 3: 5, 4: 8, 5: 11, 6: 14, 7: 17, 8: 20, 9: 23, 10: 26}
case = 0
for scores in dances:
	case += 1
	scores_lst = scores.split()
	num_dancers = int(scores_lst[0])
	surprises = int(scores_lst[1])
	top_score = int(scores_lst[2])
	dancers = scores_lst[3:]
	count = 0
	for dance in dancers:
		dance = int(dance)
		if max_dict[top_score] <= dance:
			count += 1
		elif (surprises > 0) and (dance in surp_matters) and (max_surp_dict[int(top_score)] <= dance):
			count += 1
			surprises -= 1
	string = 'Case #%d: ' %case + str(count) + '\n'
	answer.write(string)
answer.close()