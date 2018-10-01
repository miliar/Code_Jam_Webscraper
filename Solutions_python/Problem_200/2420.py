def isTidy(n):
	temp = n%10
	n /= 10
	while n:
		if n%10 > temp:
			return False
		temp = n%10
		n /= 10
	return True

t = int(raw_input())

for i in xrange(t):
	n = int(raw_input())
	ans = ""
	while n:
		if isTidy(n):
			ans = str(n) + ans
			break
		ans = "9" + ans
		if n%10 != 9:
			n /= 10
			n -= 1
		else:
			n /= 10
	print "Case #"+str(i+1)+": "+ans