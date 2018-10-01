def get_row():
	row = input()
	return set([map(int, raw_input().split()) for _ in range(4)][row-1])

for i in range(1, input()+1):
	candi = get_row() & get_row()
	if len(candi) > 1:
		print 'Case #%d: Bad magician!' % (i)
	elif len(candi) == 1:
		print 'Case #%d: %d' % (i, candi.pop())
	else:
		print 'Case #%d: Volunteer cheated!' % (i)
