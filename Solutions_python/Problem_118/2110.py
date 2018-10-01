from math import *

def is_palindrome(num):
    return str(num) == str(num)[::-1]

lines = open("C-small-attempt0.in", "r").read().splitlines()

for x in range(1, int(lines[0])+1):
	count = 0
	[first, last] = lines[x].split(" ")
	first = int(first)
	last = int(last)
	
	for i in range(int(ceil(sqrt(first))), int(floor(sqrt(last)))+1):
		if is_palindrome(i) and is_palindrome(i*i):
			#print "%d and %d are palindromes" % (i, i*i)
			count += 1
	
	print "Case #%d: %d" % (x, count)