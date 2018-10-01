#!/usr/bin/python3.1

import sys
import re
import itertools

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

def main():
	
	dat = open("C-small-attempt0.in","r")
	dat2 = open("C-small-attempt0.out","w")
	line = dat.readline()
	for t in range(0,int(line)):
		
		linija = dat.readline()
		linija = re.split(' ',linija)
		broj = int(linija[0])
		brojevi = set()
		for i in linija[1:]:
			brojevi.add(int(i))
		
		nasao = 0
		for i in range(1,broj+1):
			
			for j in findsubsets(brojevi,i):
				vrijednost = 0
				for k in j:
					vrijednost += k
				
				for k in range(1,i):
					
					for l in findsubsets(brojevi,k):
						
						vrijednost2 = 0
						for m in l:
							vrijednost2 += m
						if vrijednost == vrijednost2:
							nasao = 1
							break
					if nasao == 1:
						break
				if nasao == 1:
						break
			if nasao == 1:
						break
		dat2.write("Case #%d:\n" %(t+1))
		izlaz = ""
		for n in j:
			izlaz += " %d" %n
		izlaz = izlaz[1:] + "\n"
		dat2.write(izlaz)
		izlaz = ""
		for n in l:
			izlaz += " %d" %n
		izlaz = izlaz[1:] + "\n"
		dat2.write(izlaz)
		
	return 0

if __name__ == '__main__':
	main()
