#!/usr/bin/env python
from sys import stdin

T = int(stdin.readline())

mapping = "yhesocvxduiglbkrztnwjpfmaq"

def map(letter):
	if letter == ' ': return " "
	return mapping[ord(letter)-97]
	
for i in xrange(T):
	
	line = stdin.readline()
	translated = [map(letter) for letter in line[:-1]]
	
	print "Case #%d: %s" % (i+1, ''.join(translated))
