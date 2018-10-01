import sys

def get_cases():
	input_board = sys.stdin.read()
	num_test_cases = input_board.split('\n')[0]
	count = 0
	cases = []
	bucket = []
	for line in input_board.split('\n')[1:]:
		if count == 4:
			cases.append(bucket)
			bucket = []
			count = 0
		else:
			bucket.append(line)
			count += 1
	return cases

def check_diagonals(case,x_or_y):
	bools_left = []
	for x in range(0,4):
		if case[x][x] == x_or_y or case[x][x] == 'T':
			bools_left.append(True)
		else:
			bools_left.append(False)

	bools_right = []
	for x in range(0,4):
		if case[x][-(x+1)] == x_or_y or case[x][-(x+1)] == 'T':
			bools_right.append(True)
		else:
			bools_right.append(False)	

	if not False in bools_left or not False in bools_right:
		return True
	else: return False

def check_horizontal(cases,x_or_y):
	bools = [[] for x in range(0,4)]
	for x in range(0,len(cases)):
		bools[x] = [x_or_y==c or c=='T' for c in cases[x]]
	over_bools = [False in b for b in bools]
	return (False in over_bools)

def check_vertical(case,x_or_y):
	bools = [[] for x in range(0,4)]
	for x in range(0,4):
		for y in range(0,4):
			if case[x][y]==x_or_y or case[x][y]=='T':
				bools[y].append(True)
			else: bools[y].append(False)
	over_bools = [False in b for b in bools]
	return (False in over_bools)

def is_done(case):
	bools = [[p=='.' for p in c] for c in case]
	if True in [True in b for b in bools]: return False
	else: return True

def who_wins(case):
	players = {'X':False,'O':False}
	for player in players.keys():
		#print 'diag: ' + str(check_diagonals(case,player))
		#print 'hori: ' + str(check_horizontal(case,player))
		#print 'vert: ' + str(check_vertical(case,player))
		if check_diagonals(case,player) or check_horizontal(case,player) or check_vertical(case,player):
			players[player] = True

	if players['X'] == players['O']:
		if is_done(case): return 'Draw'
		else: return 'Game has not completed'
	if players['X'] == True: return 'X won'
	if players['O'] == True: return 'O won'

def main():
	cases = get_cases()
	for x in range(0,len(cases)):
		print 'Case #%d: %s' % (x+1, who_wins(cases[x]))

if __name__ == "__main__":
	main()
