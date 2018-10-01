#!/usr/bin/python3.3

import sys
import struct
import socket
import time
import select
import re
from optparse import OptionParser

def main():
	t = int(sys.stdin.readline())
	i = 1
	while i <= t:
		i += 1		

		array1 = []
		array2 = []
		# read first pick
		firstPick = int(sys.stdin.readline())

		# Read Array1
		line1 = sys.stdin.readline().split()
		line2 = sys.stdin.readline().split()
		line3 = sys.stdin.readline().split()
		line4 = sys.stdin.readline().split()
		array1.append(line1)
		array1.append(line2)
		array1.append(line3)
		array1.append(line4)
		
		# Read second pick
		secondPick = int(sys.stdin.readline())
		
		# Read Array2
		line1 = sys.stdin.readline().split()
		line2 = sys.stdin.readline().split()
		line3 = sys.stdin.readline().split()
		line4 = sys.stdin.readline().split()
		array2.append(line1)
		array2.append(line2)
		array2.append(line3)
		array2.append(line4)
		

		row1 = array1[firstPick-1]
		row2 = array2[secondPick-1]
		
		found = []
		for k in range(4):
			for j in range(4):
				if row1[k]==row2[j]:
					found.append(row1[k])

		if len(found) == 0:
			print("Case #",i-1,": ","Volunteer cheated!", sep='')
		elif len(found) == 1:
			print("Case #",i-1,": ", found[0], sep='')
		elif len(found) > 1:
			print("Case #",i-1,": ","Bad magician!", sep='')
			

	

if __name__ == '__main__':
    main()
