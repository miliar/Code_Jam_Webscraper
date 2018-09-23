def flipDigit(s):
	if s == '+':
		return '-'
	return '+'
def flip(index):
	for i in range(index,index+k):
		s[i] = flipDigit(s[i])
for l in range(input()):
	print "Case #"+str(l+1)+":",
	s,k = raw_input().split()
	s = list(s)
	k = int(k)
	count = 0
	for i in range(len(s)):
		if s[i]=='-':
			try:
				flip(i)
				count+=1
			except:
				count = None
				break
	if count!=None:
		print count
	else:
		print "IMPOSSIBLE"
				

