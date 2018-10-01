#!/usr/bin/python
#coding: utf-8
#autor: Nahu
#problem A

import sys
from string import maketrans 

intab  = "aozurlngeismpbtdhwyxfckjvq"
outtab = "yeqjpmslckdxvnribtahwfougz"

trantab = maketrans(outtab, intab)

input = open(sys.argv[1], "r")
lineas = input.readlines()

for i in range(1, int(lineas[0]) + 1):
    salida = "Case #" + str(i) + ": " + lineas[i].translate(trantab).strip()
    print salida
