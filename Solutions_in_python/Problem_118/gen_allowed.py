def isPalindrome(constant):
	constant = str(constant)
	length = len(constant)
	if (length % 2) == 0:
		for p in range(length/2):
			if constant[p] != constant[length-p-1]:
				return False
		return True
	else:
		for p in range((length-1)/2):
			if constant[p] != constant[length-p-1]:
				return False
		return True

fairsquare = []

for i in range(10000000):
	a = i+1
	if isPalindrome(a) == True:
		b = a**2
		if isPalindrome(b) == True:
			fairsquare.append(b)

print fairsquare
