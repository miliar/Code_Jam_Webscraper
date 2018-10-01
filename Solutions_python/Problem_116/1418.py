def solve_problem(state):
	game_on= False
	for i in range(4):
		if (state[i][0]=='X' or state[i][0]=='T') and (state[i][1]=='X' or state[i][1]=='T') and (state[i][2]=='X' or state[i][2]=='T') and (state[i][3]=='X' or state[i][3]=='T'):
			return 'X won'
		elif (state[i][0]=='O' or state[i][0]=='T') and (state[i][1]=='O' or state[i][1]=='T') and (state[i][2]=='O' or state[i][2]=='T') and (state[i][3]=='O' or state[i][3]=='T'):
			return 'O won'
		elif state[i][0]=='.' or state[i][1]=='.' or state[i][2]=='.' or state[i][3]=='.':
				game_on= True
	for i in range(4):
		if (state[0][i]=='X' or state[0][i]=='T') and (state[1][i]=='X' or state[1][i]=='T') and (state[2][i]=='X' or state[2][i]=='T') and (state[3][i]=='X' or state[3][i]=='T'):
			return 'X won'
		if (state[0][i]=='O' or state[0][i]=='T') and (state[1][i]=='O' or state[1][i]=='T') and (state[2][i]=='O' or state[2][i]=='T') and (state[3][i]=='O' or state[3][i]=='T'):
			return 'O won'
	if (state[0][0]=='X' or state[0][0]=='T') and (state[1][1]=='X' or state[1][1]=='T') and (state[2][2]=='X' or state[2][2]=='T') and (state[3][3]=='X' or state[3][3]=='T') \
		or (state[0][3]=='X' or state[0][3]=='T') and (state[1][2]=='X' or state[1][2]=='T') and (state[2][1]=='X' or state[2][1]=='T') and (state[3][0]=='X' or state[3][0]=='T'):
		return 'X won'
	elif (state[0][0]=='O' or state[0][0]=='T') and (state[1][1]=='O' or state[1][1]=='T') and (state[2][2]=='O' or state[2][2]=='T') and (state[3][3]=='O' or state[3][3]=='T') \
		or (state[0][3]=='O' or state[0][3]=='T') and (state[1][2]=='O' or state[1][2]=='T') and (state[2][1]=='O' or state[2][1]=='T') and (state[3][0]=='O' or state[3][0]=='T'):
		return 'O won'
	elif game_on:
		return 'Game has not completed'
	else:
		return 'Draw'
		
file= open('tic_tac_toe_tomek.in')
input= file.read()
file.close()

i= input.find('\n')
T= int(input[:i])
cases= input[i+1:].split('\n\n')
for i in range(1,T+1):
	state= cases[i-1].split('\n')
	print 'Case #' + str(i)	+ ': ' + solve_problem(state)
