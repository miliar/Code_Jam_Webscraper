def solve(n):
	for i, v in enumerate(n):
		if i == 0:
			continue
		if n[i-1] > v:
			return solve((str(int(n[:i])-1).lstrip('0') + '9'*(len(n)-i)))
	return n

for ln, line in enumerate(open('B-large.in')):
	if ln == 0:
		continue
	print "Case #%d: %s" % (ln, solve(line.strip()))
