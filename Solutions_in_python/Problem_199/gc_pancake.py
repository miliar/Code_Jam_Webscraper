t = input()

for ctr_does_not_matter_here in range(1,t+1):
	s = raw_input()

	s = s.split(" ")
	k = int(s[1])
	s = s[0]
	n = len(s)
	flips=0

	if('-' not in s):
		print 'Case #' + str(ctr_does_not_matter_here) + ': 0'
	else:
		for i in range(n):
			if s[i] == '-' and i+k-1<n:
				flips += 1
				for j in range(i,i+k):
					if(s[j] == '-'):
						s = s[0:j] + '+' + s[j+1:n]
					else:
						s = s[0:j] + '-' + s[j+1:n]

		if '-' in s:
			print 'Case #' + str(ctr_does_not_matter_here) + ': IMPOSSIBLE'
		else:
			print 'Case #' + str(ctr_does_not_matter_here) + ': '+str(flips)