#!/usr/bin/python

import sys



def main():
	dic = {'a': 'y', \
			'b': 'h', \
			'c': 'e', \
			'd': 's', \
			'e': 'o', \
			'f': 'c', \
			'g': 'v', \
			'h': 'x', \
			'i': 'd', \
			'j': 'u', \
			'k': 'i', \
			'l': 'g', \
			'm': 'l', \
			'n': 'b', \
			'o': 'k', \
			'p': 'r', \
			'q': 'z', \
			'r': 't', \
			's': 'n', \
			't': 'w', \
			'u': 'j', \
			'v': 'p', \
			'w': 'f', \
			'x': 'm', \
			'y': 'a', \
			'z': 'q', \
			' ': ' ' }

	a = open("input.txt","r")
	a.readline()
	count = 0
	for line in a:
		line = line.split("\n")[0]
		count += 1
		print "Case #" + str(count) + ":",
		tmpstr = ""
		for j in range(len(line)):
			tmpstr += dic[line[j]]
		print tmpstr














if __name__ == "__main__":
	main()
