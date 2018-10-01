import math

def findLimits(input_str):
	space_pos = input_str.find(' ')
	lower = int(input_str[:space_pos])
	upper = int(input_str[space_pos:])
	lower_root = int(math.sqrt(lower))
	if lower_root**2 < lower:
		lower_root += 1
	upper_root = int(math.sqrt(upper))
	if upper_root **2 <= upper:
		upper_root += 1
	return (lower_root, upper_root)

def isPalindrome(num):
	str_num = str(num)
	for i in range(len(str_num)//2):
		if str_num[i] != str_num[-(i+1)]:
			return False
	return True

nCases = int(input())
case = 0
while case < nCases:
	case += 1
	text = "Case #{0}: {1}"
	result = 0
	(lower, upper) = findLimits(input())
	for i in range(lower, upper):
		if isPalindrome(i) and isPalindrome(i**2):
			result += 1
	print(text.format(case, result))