rules = {
	'11' : ( 1, '1'),
	'1i' : ( 1, 'i'),
	'1j' : ( 1, 'j'),
	'1k' : ( 1, 'k'),
	'i1' : ( 1, 'i'),
	'j1' : ( 1, 'j'),
	'k1' : ( 1, 'k'),
	
	'ii' : (-1, '1'),
	'ij' : ( 1, 'k'),
	'ik' : (-1, 'j'),

	'ji' : (-1, 'k'),
	'jj' : (-1, '1'),
	'jk' : ( 1, 'i'),
	
	'ki' : ( 1, 'j'),
	'kj' : (-1, 'i'),
	'kk' : (-1, '1'),
}		

t = int(input())
for i in range(t):
	l, x = map(int, input().split())
	if x > 20:
		x = (x - 20) % 20 + 20
		
	s = input() * x
	if len(s) < 3:
		print('Case #%d: NO' % (i + 1))
		continue
	cur = (1, '1')
	gotI, gotJ = False, False
	for j in s:
		tmp = rules[cur[1] + j]
		cur = (cur[0] * tmp[0], tmp[1])
		if not gotI:
			if cur == (1, 'i'):
				gotI = True
				cur = (1, '1')
		elif not gotJ and cur == (1, 'j'):
			gotJ = True
			cur = (1, '1')
	if gotI and gotJ and cur == (1, 'k'):
		print('Case #%d: YES' % (i + 1))
	else:
		print('Case #%d: NO' % (i + 1))
