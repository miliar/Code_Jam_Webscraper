import math

def isPalindrome(num):
	numstr = str(num)
	for i in range(0, int(math.ceil(len(numstr)))):
		if numstr[i] != numstr[len(numstr) - i - 1]:
			return False
	return True

def countFancyPalindromes(a, b):
	n = 0
	
	for i in range(a, b + 1):
		if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)):
			if isPalindrome(int(math.sqrt(i))) and isPalindrome(i):
				n += 1
	return n

def countFancyPalindromes2(a, b):
	n = 0
	length = len(main_palindromes)
	for i in range(0, length):
		if main_palindromes[i] >= a and main_palindromes[i] <= b:
			n += 1
	return n

f = open('C-large-1.in')
output = open('C_large_output.txt', 'w')

def echo(line):
	print line
	output.write(line + '\n')

main_palindromes = []

for i in range(1, 10000000):
	if isPalindrome(i):
		if isPalindrome(i*i):
			main_palindromes.append(i*i)

n = 0
cases = int(f.readline())

for line in f:
	n = n + 1
	if n <= cases:
		nums = line.strip().split(' ')
		a = int(nums[0])
		b = int(nums[1])
		echo('Case #' + str(n) + ": " + str(countFancyPalindromes2(a, b)))

f.close()
output.close()

'''for i in range(1, 10000000):
	if isPalindrome(i):
		if isPalindrome(i*i):
			print i'''
