#https://code.google.com/codejam/contest/2974486/dashboard#s=p0

def get_result(answers, grids):
	possible = []
	possible += [grids[0][int(answers[0]) - 1]]
	possible += [grids[1][int(answers[1]) - 1]]
	occurence = []
	for card in possible[0][:-1].split(' '):
		if card in possible[1][:-1].split(' '):
			occurence += [card]
	if len(occurence) == 1:
		return occurence[0]
	elif len(occurence) > 1:
		return 'Bad magician!'
	else:
		return 'Volunteer cheated!'

with open('input.in', 'r') as raw:
	lines = raw.readlines()[1:]
	with open('output.out', 'w') as output:
		for i in range(len(lines) / 10):
			output.write('Case #%i: %s\n' % (i + 1, get_result([lines[(i + 1) * 10 - 10], lines[(i + 1) * 10 - 10 + 5]], [lines[(i + 1) * 10 - 10 + 1: (i + 1) * 10 - 10 + 5], lines[(i + 1) * 10 - 10 + 6: (i + 1) * 10 - 10 + 10]])))