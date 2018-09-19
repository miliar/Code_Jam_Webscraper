# -*-coding:utf-8 -*

import sys
from os import system

def solve(t):
	C = float(t[0])
	F = float(t[1])
	X = float(t[2])
	gain = 2
	Time = float(0)
	bool = True
	while bool is True:
		T_farm = C/gain 
		T_f_m = X/(gain + F)
		T_win = X/gain
		if (T_farm + T_f_m) < T_win:
			gain += F
			Time += T_farm
		else:
			Time += T_win
			bool = False
	return str("%.7f" % Time)


entree = open("./B-large.in", "r")
sortie = open("./B-large.out", "w")
numcases = int(entree.readline())
for casenum in range(1,numcases+1):
	tab = entree.readline().split()
	s = str("Case #" + repr(casenum) + ": " + solve(tab)+'\n')
	sortie.write(s)
entree.close()
sortie.close()
