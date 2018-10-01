import operator

t = int(input())

for case_num in range(t):
	line = [int(x) for x in input().split(' ')]
	ac = int(line[0])
	aj = int(line[1])
	jc = []
	jj = []
	for i in range(ac):
		line = [int(x) for x in input().split(' ')]
		s = int(line[0])
		e = int(line[1])
		jc.append((s, e))
	for i in range(aj):
		line = [int(x) for x in input().split(' ')]
		s = int(line[0])
		e = int(line[1])
		jj.append((s, e))
	if ac > 0:
		jc.sort(key=operator.itemgetter(0))
		merge = [jc[0]]
		for i in range(ac - 1):
			if merge[-1][1] == jc[i + 1][0]:
				merge[-1] = (merge[-1][0], jc[i + 1][0])
			else:
				merge.append(jc[i + 1])
		jc = merge

	if aj > 0:
		jj.sort(key=operator.itemgetter(0))
		merge = [jj[0]]
		for i in range(aj - 1):
			if merge[-1][1] == jj[i + 1][0]:
				merge[-1] = (merge[-1][0], jj[i + 1][0])
			else:
				merge.append(jj[i + 1])
		jj = merge
	if len(jc) == 0:
		if len(jj) == 2 and jj[1][1] - jj[0][0] > 720 and jj[0][1] + 1440 - jj[1][0] > 720:
			ans = 4
		else:
			ans = 2
	elif len(jj) == 0:
		if len(jc) == 2 and jc[1][1] - jc[0][0] > 720 and jc[0][1] + 1440 - jc[1][0] > 720:
			ans = 4
		else:
			ans = 2
	else:
		ans = 2;
	print('Case #%d: %d' % (case_num + 1, ans))
