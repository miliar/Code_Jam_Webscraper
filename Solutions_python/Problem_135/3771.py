
def solve(i):
	ans = int(raw_input())
	for j in xrange(1,5):
		if j == ans:
			row = raw_input()
		else:
			raw_input()
	
	ans2 = int(raw_input())
	for j in xrange(1,5):
		if j == ans2:
			row2 = raw_input()
		else:
			raw_input()
	
	row = row.split()
	row2 = row2.split()

	ans = -1
	for a in row:
		for b in row2:
			if a == b and ans > 0:
				print 'Case #'+str(i)+ ': Bad magician!'
				return
			elif a == b:
				ans = int(a)
	if ans > 0:
		print 'Case #'+str(i)+ ': '+str(ans)
	else:
		print 'Case #'+str(i)+ ': Volunteer cheated!'

T = int(raw_input())
for i in xrange(1, T+1):
	solve(i)
