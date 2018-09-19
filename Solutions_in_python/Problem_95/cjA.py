#!/usr/bin/env python
#-*- coding:utf-8 -*-

from string import *
import string

fichero_in = open("/home/blacknack/Escritorio/A-small-attempt0.in", "r")
fichero_out = open ("/home/blacknack/Escritorio/aout.txt", "w")

nlineas = int(fichero_in.readline())

intab = string.lowercase
outtab = "ynficwlbkuomxsevzpdrjgthaq"
tab = maketrans(outtab, intab)


for i in range(nlineas):
	res = ""
	linea = fichero_in.readline()
	l = linea.split()
	for word in l:
		res += word.translate(tab) + " "
	fichero_out.write("Case #" + str(i+1) + ": ")
	fichero_out.write(res + "\n")

