
def tidy(k):
	while 1:
		snum = list(str(k))
		r = len(snum)-1
		l = r - 1
		while l >= 0:
			if snum[r] >= snum[l]:
				l -= 1
				r -= 1
				continue
			
			m = r
			while m < len(snum):
				snum[m] = '9'
				m += 1
			if snum[l] > '0':
				snum[l] = str(int(snum[l])-1)
			else:
				snum[l] = '9'
		
		if snum[0] == '0':
			snum = snum[1:]
		
		return "".join(snum)
		
case = int(raw_input())
for c in range(1, case+1):
	number = int(raw_input())
	print "Case #"+str(c)+": " + str(tidy(number))
