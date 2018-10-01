#!/usr/bin/env python3

def read_ints():
	return map(int, input().strip().split())

T, = read_ints()

for t in range(T):
	n, = read_ints()
	t1 = [ read_ints() for _ in range(4) ]
	m, = read_ints()
	t2 = [ read_ints() for _ in range(4) ]
	n-=1
	m-=1

	inter = set(t1[n]).intersection(set(t2[m]))

	if len(inter)==1:
		x, = list(inter)
		ans = str(x)
	elif len(inter)==0:
		ans = 'Volunteer cheated!'
	else:
		ans = 'Bad magician!'

	print('Case #{}: {}'.format(t+1, ans))
		
