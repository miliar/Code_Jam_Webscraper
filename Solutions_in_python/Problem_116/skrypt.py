#!/usr/bin/python

import re
import sys

wyniki={"X":"Case #%d: X won",
		"O":"Case #%d: O won",
		"D":"Case #%d: Draw",
		"G":"Case #%d: Game has not completed"
		}

if len(sys.argv)>1 :
    plik=open(sys.argv[1])
    dane=plik.readlines()
else:
    dane=sys.stdin.readlines()


liczba=int(dane[0].strip())


for x in range(0,liczba):
    tablica=dane[(1+x*5):(5+x*5)]
    tablica=map(lambda a: a.strip(), tablica)
    tablica="".join(tablica)
    X=tablica.replace("T","X")
    O=tablica.replace("T","O")
    wynik="D"
    if (X[0:4] == "XXXX" or X[4:8] == "XXXX" or X[8:12] == "XXXX" or X[12:16] == "XXXX" or X[0:16:5] == "XXXX" or X[3:13:3] == "XXXX" or X[3:16:4] =="XXXX" or X[2:16:4] =="XXXX" or X[1:16:4] =="XXXX" or X[0:16:4] =="XXXX"):
        wynik="X"
    elif (O[0:4] == "OOOO" or O[4:8] == "OOOO" or O[8:12] == "OOOO" or O[12:16] == "OOOO" or O[0:16:5] == "OOOO" or O[3:13:3] == "OOOO" or O[3:16:4] =="OOOO" or O[2:16:4] =="OOOO" or O[1:16:4] =="OOOO" or O[0:16:4] =="OOOO"):
        wynik="O"
    elif tablica.count(".")>0:
        wynik="G"
    print wyniki[wynik] % (x +1)
	
    	    	

        

