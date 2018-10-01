# https://code.google.com/codejam/contest/3264486/dashboard

def flip(s, k):
	for i in range(k):
		if s[i] == "+":
			s[i] = "-"
		else:
			s[i] = "+"
	return s

def pancakeFlipper(s, k):
	n = len(s)
	i = 0
	res = 0
	while i <= n - k:
		if s[i] == '-':
			s[i : i + k] =  flip(s[i : i + k], k)
			res += 1
		i += 1
	if '-' in s:
		return 'IMPOSSIBLE'
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		s, k = (raw_input().split())
		s = list(s)
		k = int(k)
		print "Case #{}:".format(i), pancakeFlipper(s, k)
