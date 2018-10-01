def is_tidy(num):
	num = str(num)
	last = "0"
	for n in num:
		if int(n) < int(last):
			return False
		last = n
	return True

t = int(input())

for case in range(1, t + 1):
	n = int(input())
	if is_tidy(n):
		print("Case #%d: %s" % (case, n))
	else:
		tidy_num = 0
		for i in range(1, len(str(n))):
			num = n // (10 ** i) * (10 ** i) - 1
			if is_tidy(num):
				tidy_num = num
				break
		print("Case #%d: %d" % (case, tidy_num))
