#!/usr/bin/env python
import sys
import re
from sets import Set

COMB = {}
REM = Set()

def main():
	T = raw_input()
	for t in range(int(T)):
		L = raw_input().split()

		C = int(L[0])
		CA = L[1:C+1]
		D = int(L[C+1])
		DA = L[C+2:C+2+D]
		I = int(L[C+D+2])
		IA = list(L[C+D+3:][0])

		COMB = {}
		REM = Set()

		for i in CA:
			COMB[(i[0],i[1])]=i[2]
			COMB[(i[1],i[0])]=i[2]
		for i in DA:
			REM.add(((i[0],i[1])))
			REM.add(((i[1],i[0])))

		L = []
		for i in IA:
			L.append(i)
			LL = len(L)
			if(LL >= 2):
				K = (L[LL-1], L[LL-2])
				if K in COMB:
					V = COMB[K]
					L = L[0:LL-2]
					L.append(V)
					LL = len(L)
#				else:
#					break
			if(len(L) >= 2):
				for i in L[:-1]:
					K = (i,L[len(L)-1])
					if K in REM:
						L = []
						break

	
		print "Case #"+str(t+1)+": " + str(L).replace("'","")

if __name__ == "__main__":
    main()
