def check(*args):
	o_cnt = x_cnt = t_cnt = 0
	has_dot = False

	for arg in args[0]:
		if arg == 'O':
			o_cnt += 1
		elif arg == 'X':
			x_cnt += 1
		elif arg == 'T':
			t_cnt += 1
		elif arg == '.':
			has_dot = True
			continue
		else:
			print('f*ck: {}'.format(arg))

	if o_cnt == 4 or (o_cnt == 3 and t_cnt == 1):
		return True, 'O', has_dot
	elif x_cnt == 4 or (x_cnt == 3 and t_cnt == 1):
		return True, 'X', has_dot
	else:
		return False, '', has_dot


def game(*args):
	ok = False
	win = ''

	for j, horz in enumerate(args):
		ok, win, dot = check(tuple(horz[i] for i in range(4)))
		if ok: break

		ok, win, dot = check(tuple(args[i][j] for i in range(4)))
		if ok: break

	if not ok:
		ok, win, dot = check(tuple(args[i][i] for i in range(4)))
	if not ok:
		ok, win, dot = check(tuple(args[i][3-i] for i in range(4)))

	if ok:
		return win + ' won'
	elif dot:
		return 'Game has not completed'
	else:
		return 'Draw'


def mainFromFile(filename):
	text = ''

	f = open(filename, 'r')
	T = int(f.readline())

	for i in range(T):
		l0 = f.readline()
		l1 = f.readline()
		l2 = f.readline()
		l3 = f.readline()
		l4 = f.readline()

		result = game(l0, l1, l2, l3)
		text += 'Case #{}: {}\n'.format(i + 1, result)

	f.close()

	return text


def mainFromNogada():
	text = ''

	result = game(
		'XXXT',
		'....',
		'OO..',
		'....'
	)
	text += 'Case #1: {}\n'.format(result)

	result = game(
		'XOXT',
		'XXOO',
		'OXOX',
		'XXOO'
	)
	text += 'Case #2: {}\n'.format(result)

	result = game(
		'XOX.',
		'OX..',
		'....',
		'....'
	)
	text += 'Case #3: {}\n'.format(result)

	result = game(
		'OOXX',
		'OXXX',
		'OX.T',
		'O..O'
	)
	text += 'Case #4: {}\n'.format(result)

	result = game(
		'XXXO',
		'..O.',
		'.O..',
		'T...'
	)
	text += 'Case #5: {}\n'.format(result)

	result = game(
		'OXXX',
		'XO..',
		'..O.',
		'...O'
	)
	text += 'Case #6: {}\n'.format(result)

	return text


if __name__ == '__main__':
	#text = mainFromNogada()
	text = mainFromFile('A-small-attempt2.in')

	f = open('result.txt', 'w')
	f.write(text)
	f.close()

