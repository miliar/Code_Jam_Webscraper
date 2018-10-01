import fileinput

f = fileinput.input()
nc = int(f.readline().strip())
for c in range(nc):
	a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
	for _ in range(2):
		j = int(f.readline())
		bs = [f.readline().strip() for _ in range(0, 4)]
		a &= set(int(x) for x in bs[j - 1].split())
	print 'Case #%s: %s' % (c+1, list(a)[0] if len(a) == 1 else 'Bad magician!' if len(a) > 0 else 'Volunteer cheated!')










