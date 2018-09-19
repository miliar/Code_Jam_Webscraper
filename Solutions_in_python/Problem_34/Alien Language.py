#!/usr/bin/env python
# encoding: utf-8
"""
Alien Language.py

Created by Devon Proctor on 2009-09-03.
Copyright (c) 2009 Stanford University. All rights reserved.
"""

import sys
import os
import string

def main():
	writefile = open('large_output.txt', 'w')
	readfile = open('A-large.in')
	
	lines = readfile.readlines()
	
	settings = lines.pop(0).split()
	L = int(settings[0])
	D = int(settings[1])
	N = int(settings[2])
	
	words = list()
	
	for i in range(D):
		word = lines.pop(0)
		word = word[:L]
		words.append(word)
	
	answers = list()
	
	for i in range(N):
		wordinfo = lines.pop(0)
		wordsleft = words
		
		for j in range(L):
			if wordinfo[0] == '(':
				possibleletters = list(wordinfo[1:string.find(wordinfo, ')')])
				wordinfo = wordinfo[len(possibleletters) + 2:]
			else:
				possibleletters = list(wordinfo[0])
				wordinfo = wordinfo[1:]
						
			qualifiedwords = list()
			
			for w in wordsleft:
				if w[j] in possibleletters:
					qualifiedwords.append(w)
			wordsleft = qualifiedwords
		
		printCase(writefile, i+1, len(wordsleft))
	
	writefile.close()



	
def printCase(f, index, num):
	"""docstring for printCase"""
	f.write("Case #{0}: {1}\n".format(index, num))



if __name__ == '__main__':
	main()

