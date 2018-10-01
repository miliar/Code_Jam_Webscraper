#!/usr/bin/python
#coding: utf-8

fin = file('A-small-attempt0.in', 'r')
fout = file('A-small-attempt0.out', 'w')

from decimal import *
import math

getcontext().prec = 100

fin.readline()
case = 0
for line in fin.readlines():
	if line[-1] == '\n': line = line[:-1]
	rs, ts = line.split()
	r, t = long(rs), long(ts)

	ret = (Decimal(1 - 2 * r) + Decimal((2 * r - 1) * (2 * r - 1) + 8 * t).sqrt()) / Decimal(4.0)
	ret = int(math.floor(ret))
	case += 1
	fout.write('Case #' + str(case) + ': ' + str(ret) + '\n')
	# print ret
