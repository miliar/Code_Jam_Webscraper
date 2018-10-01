def solve(info):
	(s,k)=info.split(" ")
	s=list(s)
	k=int(k)
	q=0
	for i in range(0,len(s)):
		if s[i]=='+':
			continue
		try:
			for z in range(0,k):
				if s[i+z]=='+':
					s[i+z]='-'
				elif s[i+z]=='-':
					s[i+z]='+'
			q=q+1
		except:
			return 'IMPOSSIBLE'
	return q

if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases + 1):
		info = raw_input()
		print("Case #%i: %s" % (caseNr, solve(info)))
