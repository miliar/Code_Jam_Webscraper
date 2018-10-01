def is_tidy(n):
	prev = n % 10

	while (n > 0):
		n = n / 10
		if (n % 10 > prev):
			return False
		prev = n % 10
	return True

def tidy(n):
	while (not is_tidy(n)):
		n -= 1
	return n;

t = int(raw_input().strip())
for a0 in range(t):
	n = int(raw_input().strip())
	print("Case #%d: %d" % (a0 + 1, tidy(n)))