#!/usr/bin/env python
import string
import math
from numpy  import *

ipt = open("q3l.i", "r")
opt = open("q3l.o", "w+")

cases = int(ipt.readline())
#print cases

def itoa(num, radix): 
	result = "" 
	while num > 0: 
		result = "0123456789abcdefghijklmnopqrstuvwxyz"[num % radix] + result 
		num /= radix 
	return result 

ll = [0,]
cnt = 1

while cnt < 100000000000000 :
	a = itoa(cnt,3)

	if cnt == 3 :
		ll.append(9)
		cnt += 1
		continue
	
	test1 = list(a)
	test2 = list(a)
	test2.reverse()
	if test1 != test2 :
		cnt += 1
		continue
	b = int(a)*int(a)

	if b > 100000000000000 : break
	test3 = list(str(b))
	test4 = list(str(b))
	test4.reverse()
	if test3 == test4 :
		ll.append(b)
	cnt+=1

ll.append(100000000000001)
#print ll

for case in range(cases) :
	case = case+1
	input = ipt.readline().rsplit()
	A = int(input[0])
	B = int(input[1])
#	print A, B

	count = 0
	start = 0
	end = 0

	for a in range(41) :
#		print a, A, ll[a], ll[a-1]
		if ll[a] >= A and ll[a-1] < A:
			start = a
		if ll[a] > B and ll[a-1] <= B :
			end = a
			break
#	print start, end, end - start 

	print("Case #%i: %i" % (case, end - start))
	opt.write("Case #%i: %i\n" % (case, end - start))

ipt.close()
opt.close()

