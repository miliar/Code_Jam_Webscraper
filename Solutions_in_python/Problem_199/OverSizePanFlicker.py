
T = int(raw_input())

for t in range(0,T):

	s,ki = raw_input().split()

	k = int(ki)

	count = 0
	modified = 0

	for l in range(0,len(s)-k+1):
		modified = 0

		if s[l] == '-':
			count = count + 1
			modified = 1
			subStr = ""
			for c in range(l,l+k):
				if s[c] == '-':
					subStr = subStr + '+' 
				else:
					subStr = subStr + '-' 

		if modified == 1:
			s = s[:l] + subStr + s[l+k:]
			#print s

	success = 1
	for l in range(0,len(s)):
		if s[l] == '-':
			success = 0
			break
	if success == 0:
		print "Case #"+ str(t+1) + ": " + "IMPOSSIBLE"
	else:
		print "Case #"+ str(t+1) + ": " + str(count)

