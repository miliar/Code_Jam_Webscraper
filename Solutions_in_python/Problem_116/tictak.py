input_file = open("A-small-attempt1.in", 'r')
output_file = open("output.txt",'w')
no_of_cases = input_file.readline().strip()
winning_moves = [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15], # vertical
                        [0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15], # horizontal
                        [0,5,10,15],[3,6,9,12]]         # diagonal

for i in range(1,int(no_of_cases)+1):
	board = []
	row1 = input_file.readline().strip()
	row2 = input_file.readline().strip()
	row3 = input_file.readline().strip()
	row4 = input_file.readline().strip()
	board = list(row1) + list(row2) + list(row3) + list(row4)
	input_file.readline().strip()
	Draw = True
	for row in winning_moves:
		data2 = [board[x] for x in row]
		data = {j: data2.count(j) for j in set(data2)}
		if len(data) == 2:
		 	if data.keys().__contains__('T') and data.keys().__contains__('X'):
		 		output_file.write("Case #{}: X won\n".format(i))
		 		Draw = False 
		 		break
		 	elif data.keys().__contains__('T') and data.keys().__contains__('O'):
		 		output_file.write("Case #{}: O won\n".format(i))
		 		Draw = False
		 		break
		elif len(data) == 1 and  data.keys().__contains__('X'):
		 		output_file.write("Case #{}: X won\n".format(i))
		 		Draw = False
		 		break
		elif len(data) == 1 and data.keys().__contains__('O'):
		 		output_file.write("Case #{}: O won\n".format(i))
		 		Draw = False
		 		break
		elif len(data) == 1 and data.keys().__contains__('.'):
		 		output_file.write("Case #{}: Game has not completed\n".format(i))
		 		Draw = False
		 		break
	if Draw:
		check_draw_data = set(board)
		if check_draw_data.__contains__('.'):
			output_file.write("Case #{}: Game has not completed\n".format(i))
		else:
			output_file.write("Case #{}: Draw\n".format(i))
		 	