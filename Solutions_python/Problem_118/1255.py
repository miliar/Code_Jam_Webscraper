#!/usr/bin/python3
# coding=utf-8
import math
import itertools

"""
0 0
1 1
4 2
9 3
121 11
484 22
10201 101
12321 111
14641 121
40804 202
44944 212
1002001 1001
1234321 1111
4008004 2002
100020001 10001
102030201 10101
104060401 10201
121242121 11011
123454321 11111
125686521 11211
400080004 20002
404090404 20102
"""

def main():
	f = open('../test_files/input', 'r')
	w = open('../test_files/output', 'w')
	s = f.readline()
	t = int(s)
	for i in range(1, t+1):
		w.write('Case #%d: ' % i)
		(a, b) = [int(x) for x in f.readline()[:-1].split()]
		sum = 0
		for j in range(a, b+1):
			if fair(j):
				sum += 1
		w.write(str(sum) + '\n')
	w.close()

"""
def block(pow, lt, ut):
	if pow == 0:
		# подходящие числа - 0, 1, 2, 3
		return len(filter(lambda x: x >= lt and x <= ut, [0, 1, 2, 3]))
	# считая всё от 10^pow+1 до 10^(pow+1)-1
	has_axis = pow % 2 == 0
	number = "0"*(pow / 2) + "1"
	sum = 0
	p = 0
	while True:
		n = constr(number)
		if n > ut: break
		if 
	return sum
	
def constr(n, ha):
	return int((n[:-1][::-1] if ha else n[::-1]) + n)
"""
	
def pal(d):
	return str(d) == str(d)[::-1]

def fair(d):
	s = int(math.sqrt(d))
	return s * s == d and pal(d) and pal(int(math.sqrt(d)))

if __name__ == '__main__':
	main()