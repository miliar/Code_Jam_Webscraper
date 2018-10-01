#!/usr/bin/env python


def mult(x, y):
	if x[0] == "-":
		x_sign = 1
		x = x[1]
	else:
		x_sign = 0
	if y[0] == "-":
		y_sign = 1
		y = y[1]
	else:
		y_sign = 0
	answer_sign  = ( x_sign + y_sign ) % 2
	if answer_sign == 1:
		answer_sign = "-"
	else:
		answer_sign = ""
	
	ans = ""
	if x == "1":
		ans = y
	elif x == "i":
		if y == "1":
			ans= "i"
		elif y == "i":
			ans = "-1"
		elif y == "j":
			ans = "k"
		elif y == "k":
			ans = "-j"	
	elif x == "j":
		if y == "1":
			ans= "j"
		elif y == "i":
			ans = "-k"
		elif y == "j":
			ans = "-1"
		elif y == "k":
			ans = "i"	
	elif x == "k":
		if y == "1":
			ans= "k"
		elif y == "i":
			ans = "j"
		elif y == "j":
			ans = "-i"
		elif y == "k":
			ans = "-1"	
		
	if ans[0] == "-":
		if answer_sign == "-":
			return ans[1]
		else:
			return ans
	else:
		return answer_sign + ans

import sys
cases = int(sys.stdin.readline())
def go1(chars,length):
	pos = 0
	part1 = []
	part2 = []
	val = chars[pos]
	if val == "i":
		part1.append(pos)
	pos += 1
	while pos < length:
		val = mult(val,char[pos])
		if val == "i":
			part1.append(pos)
		pos += 1
	part1 = part1[0:70]
	for p in part1:
		pos = p + 1 
		if pos >= length:
			return False
		val = char[pos]
		if val == "j":
			part2.append(pos)
		pos += 1
		while pos < length:
			val = mult(val,char[pos])
			if val == "j":
				part2.append(pos)
			pos += 1
	part2 = part2[0:70]
	for  p in part2:
		pos = p +1
		if pos >= length :
			return False
		val = char[pos]
		pos += 1
		while pos < length:
			val = mult(val,char[pos])
			pos += 1
		if val == "k":
			return True

	return False
		
		

for case in range(1,cases+1):
	line = sys.stdin.readline()
	(L , X ) = line.split()
	char = sys.stdin.readline()
	char = char[:-1] * int(X)
	length = len(char) 
	ret = go1(char,length)
	if ret:
		print "Case #%d: YES" % (case)
	else:
		print "Case #%d: NO" % (case)
	
		
		
