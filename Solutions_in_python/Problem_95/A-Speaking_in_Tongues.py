#!/bin/python
# -*- coding: utf-8 -*-


_input_file = 'A-small-attempt0.in'


from collections import deque
from math import log10
import sys
from time import clock


_mapping = {
'a': 'y',
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
' ': ' '
}


def proceed(lines):
	i = 0
	nb_input = len(lines)

	while i < nb_input:
		i = i + 1
		sys.stdout.write('Case #'+ str(i) +': ')
		sys.stdout.flush()

		line = map(lambda s: _mapping[s], list(lines.popleft()))
		print ''.join(line)


def read_input():
	inputfile = open(_input_file, 'r')
	lines = deque(filter(lambda l : l, map(lambda l : l.strip(), inputfile.read().splitlines())))
	lines.popleft()
	return lines

lines = read_input()
proceed(lines)

