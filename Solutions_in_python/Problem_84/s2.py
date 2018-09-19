#!/usr/bin/env python

import sys, os

def main():
	#f = file("test.in")
	#f = file("A-small-attempt0.in")
	f = file("A-large.in")
	T = int(f.readline())
	for i in range(T):
		R, C = map(int, f.readline().strip().split())
		data = []
		for r in range(R):
			#for c in range(C):
			data.append(list(f.readline().strip()))
		#print data
		is_impossible = False
		for r in range(R):
			for c in range(C):
				#print r, c
				if data[r][c] == '#':
					if r == R - 1 or c == C - 1:
						is_impossible = True
						break;
					elif data[r][c+1] == '#' and data[r+1][c] == '#' and data[r+1][c+1] == '#':
						data[r][c] = '/'
						data[r][c+1] = '\\'
						data[r+1][c] = '\\'
						data[r+1][c+1] = '/'
					elif data[r][c+1] == '#' or data[r+1][c] == '#' or data[r+1][c+1] == '#':
						is_impossible = True
						break;
			if is_impossible:
				break

		print "Case #%s:" % (i + 1)
		if is_impossible:
			print "Impossible"
		else:
			for l in data:
				for c in l:
					sys.stdout.write(c)
				print
		

if __name__ == "__main__": main()
