#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	CodeJam 2012: Qualification Round
#	Author: Mahmoud Aladdin (Platter)
#
file_in = open("A.in", 'r')
file_out = open("A.out", "w")
	

# ======================================
filereadLine = lambda: file_in.readline().strip()
filereadInt = lambda: int(file_in.readline().strip())
filereadInts = lambda: map(int, file_in.readline().strip().split(' '))
# ======================================
import math
# ======================================


def main():
	convert = {'a' : 'y' , 'c':'e', 'd':'s', 'e':'o','f':'c', 'g': 'v', 'i':'d',  
						'j':'u', 'k':'i','l':'g', 'm':'l', 'n':'b', 'o': 'k', 'p': 'r',
						'r':'t', 's': 'n', 't':'w', 'u':'j', 'v': 'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q',
						'b':'h', 'q':'z','h': 'x', ' ':' '}
	num = filereadInt()
	for i in xrange(1, num + 1):
		msg = filereadLine()
		out = "Case #{}: ".format(i)
		for ch in msg:
			out += convert[ch]
		out += '\n'
		file_out.write(out)

	return 0
if __name__ == '__main__':
	main()
