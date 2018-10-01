def solve(N):
	if len(N) == 1:
		return N
	s = ""
	broke = False
	for i in range(len(N) - 1):
		d1 = int(N[i])
		d2 = int(N[i+1])
		if d1 <= d2:
			s += str(d1)
		else:
			s += str(d1-1)
			for j in range(i+1,len(N)):
				s += "9"
			broke = True	
			break
	if not broke:
		s += N[-1]
	if s[0] == "0":
		s = s[1:]
	if s != N:
		s = solve(s)
	return s

if __name__ == "__main__":
	t = int(raw_input())
	for i in xrange(1, t + 1):
		n = raw_input()
		answer = solve(n)
		print "Case #" + str(i) + ":",answer
