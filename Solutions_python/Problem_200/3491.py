def tidyNumbers(n):
	if len(n) <= 1:
		return n

	num = list(n)

	i = len(num) - 1

	while i > 0:
		if num[i-1] > num[i]:

			num[i] = '9'
			if num[i-1] == '0':
				num[i-1] = '9'
			else:
				num[i-1] = chr(ord(num[i-1])-1)

			j = i + 1
			while j < len(num) and num[j-1] > num[j]:
				num[j] = '9'
				j += 1

		i -= 1


	if num[0] == '0' and len(num) > 1:
		num = num[1:]
	return ''.join(num)


# n = '132'
# print tidyNumbers(n)


# n = '1000'
# print tidyNumbers(n)

# n = '7'
# print tidyNumbers(n)

	
# n = '111111111111111110'
# print tidyNumbers(n)


# n = '0'
# print tidyNumbers(n)


# n = '10'
# print tidyNumbers(n)

# n = '100100'
# print tidyNumbers(n)

# n = '1010' # 999
# print tidyNumbers(n)

# n = '1012' # 999
# print tidyNumbers(n)

# n = '5867' # 5799
# print tidyNumbers(n)

# read a line with a single integer
t = int(raw_input())

for i in xrange(1, t+1):
	# read a list of integers, 2 in this case
	n = raw_input()
	result = tidyNumbers(n)
	print "Case #{}: {}".format(i, result)