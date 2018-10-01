#!/usr/bin/env python

import string

ipt = open("q3s.i", "r")
opt = open("q3s.o", "w+")

maximum = 3000

cases = int(ipt.readline())
#print cases
base = {}

for check in range(maximum+1) : 
	if check == 0 : continue
	base[check] = set()
#	base[check].add(check)
	for aa in range(len(str(check))) :
		bb = int(str(check)[aa:len(str(check))]+str(check)[0:aa])
		if len(str(check)) == len(str(bb)) and bb <= maximum :
			base[check].add(bb)

#	print len(base[check]),check,base[check]

for case in range(cases) :
	
	input = ipt.readline().rsplit()
	A = int(input[0])
	B = int(input[1])
#	print A, B

	found = set(range(A,B+1))

	count = 0

	for aa in range(A, B+1) :
		oo = set(range(B+1,maximum+1))
		oa = set(range(1, A))
		tou = base[aa] - oo - oa
#		print A, B,aa, tou
		if aa in found and len(tou) > 1 :
			found = found - tou
#			print len(tou)*(len(tou)-1)/2
			count=count+len(tou)*(len(tou)-1)/2
		

	print( "Case #%d: %d %d %d" % (case+1, A, B, count))

	opt.write("Case #%d: %d\n" % (case+1, count))

ipt.close()
opt.close()




