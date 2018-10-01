#!/usr/bin/env python
import string

ipt = open("q1s.i", "r")
opt = open("q1s.o", "w+")

in_table  = "ynficwlbkuomxsevzpdrjgthaq"
out_table = "abcdefghijklmnopqrstuvwxyz"
trans_table = string.maketrans(in_table,out_table)

case = ipt.readline()
case = 0

for line in ipt:
	print line
	case=case+1
	line.strip()
	out_string = line.translate(trans_table)

	print out_string

	opt.write("Case #%d: %s" % (case, out_string))

ipt.close()
opt.close()




