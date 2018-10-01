import math

def palindrome(num):
	if num < 10:
		return True	
	
	else:
		snumber = list(str(num))
		snumber.reverse()
		if num == int(''.join(snumber)):
			return True

	return False

fi = open("C-small-attempt0.in","rU")
fo = open("C-small-attempt0.out","w")
T = int(fi.readline())
for test in range(T):
	AB = [int(i) for i in fi.readline().split()]
	
	sum = 0
	
	for c in range(AB[0], AB[1]+1):
		if palindrome(c):
			n = math.sqrt(c)
			if n-int(n) == 0:
				n = int(n)
				if palindrome(n):
					sum += 1

	print("Case #%d: %d" % (test+1,sum))
	fo.write("Case #%d: %d\n" % (test+1,sum))

fi.close()
fo.close()
	