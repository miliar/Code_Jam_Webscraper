#!/usr/bin/python
import math

def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n / 10, partial * 10 + n % 10)

def check_fair(number):
	rev = reverse_number(number)
	return rev == number
	
def check_square(number):
	ok = False
	root = math.sqrt(number)
	if root % 1 == 0:
		ok = check_fair(int(root))
	return ok


f = open("C-small-attempt0.in", "r")
cases = int(f.readline())

for case in range(cases):
	line = f.readline()
	ranges = line.split()
	min_range = int(ranges[0])
	max_range = int(ranges[1]) + 1
	
	fair_square = 0
	for num in range (min_range, max_range):
		fair = check_fair(num)
		if fair:
			square = check_square(num)
			if square:
				fair_square += 1
		
	print "Case #"+str(case+1)+": "+str(fair_square)
	

f.close()