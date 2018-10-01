#!/usr/bin/python
import sys

translate = {'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r', 
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm', 
 'y': 'a',
 'z': 'q',
 ' ':' ',
 '\n': '' }
		
data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	temp = data.pop(0)
	sys.stdout.write("Case #" + str(case) + ": ")
	for c in temp:
		sys.stdout.write(translate[c])
	sys.stdout.write("\n")
	case += 1