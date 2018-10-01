def solve(s, k):
	if s.count('+') == len(s):
		return '0'
	c = 0 # count
	t = list(s) # copy of string
	B = False
	while len(t) > k:
		if t[0] == '+':
			t = t[1:]
			continue
		c += 1
		for i in range(k):
			t[i] = '+' if t[i] == '-' else '-'
	
	if t.count('-') == k:
		c += 1
		B = True
	elif t.count('+') == k:
		B = True
	else: B = False
	return str(c) if B else 'IMPOSSIBLE'

if __name__ == '__main__':
	t = int(input())
	for test in range(1, t+1):
		s, k = input().split(' ')
		print('Case #%d: %s' % (test, solve(s, int(k))))