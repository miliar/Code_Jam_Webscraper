def tidyNumber(n):
	strn = str(n)
	for i in range(1, len(strn)):
		if strn[i] < strn[i-1]:
			return False
	return True

T = input()
for t in range(T):
	N = input()
	curTidyNumber = 1
	for n in range(1, N+1):
		if tidyNumber(n):
			curTidyNumber = n
	print 'Case #'+str(t+1)+': '+str(curTidyNumber)