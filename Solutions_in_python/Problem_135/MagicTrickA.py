n = int(input())
for i in range(n):
	st = input()
	st_row = set([input() for i in range(4)][int(st)-1].split())
	nd = input()
	nd_row = set([input() for i in range(4)][int(nd)-1].split())
	ans = st_row.intersection(nd_row)
	if len(ans)==1:
		sans = ans.pop()
	elif len(ans)==0:
		sans = 'Volunteer cheated!'
	else:
		sans = 'Bad magician!'
	print('Case #{}: {}'.format(i+1, sans))


