#!/usr/bin/python
from collections import deque
from decimal import *

'''
Ahmed Medhat Othman
AMedOs
amedhat.cs@gmail.com
'''

def main():
	fin = open('C-small-attempt0.in', 'r')
	fout = open('C.out','w')
	T = long(fin.readline())
	for tc in range(1,T+1):
		mn, mx = map(long, fin.readline().split())
		
		def is_pal(num):
			s = str(num)
			l =len(s)
			f = True
			for i in range(l/2):
				if s[i] != s[l-i-1]:
					f = False
					break
			
			return f

		res = 0
		for i in range(mn,mx+1):
			if int(i**0.5) == i**0.5 and is_pal(i) and is_pal(int(i**0.5)):
				res+=1

		fout.write("Case #" + str(tc) + ": " + str(res) +"\n")

if __name__ == '__main__':
	main()
