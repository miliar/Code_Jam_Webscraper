#!/usr/bin/python
import sys


my_map = {' ':' ','a': 'y', 'b':'h', 'c': 'e', 'e': 'o', 'j': 'u', 'p': 'r', 'm': 'l', 'y': 'a', 's': 'n', 'l': 'g', 'k': 'i', 'd': 's', 'x': 'm', 'v': 'p', 'r': 't', 'n': 'b', 'i': 'd', 't': 'w', 'h': 'x', 'w': 'f', 'f': 'c', 'o': 'k', 'u': 'j', 'g': 'v', 'z': 'q', 'q': 'z'}

def translate(line):
	new_line = []
	for i in line:
		try: 
			caracter = my_map[i]
			new_line.append(caracter)
		except:
			new_line.append('-')

	return "".join(new_line)


fd = open(sys.argv[1])
n_case = fd.readline()

count = 1
for line in fd.readlines():
	line = line.strip()
	print "Case #%s: %s" % (count, translate(line))
	count += 1





