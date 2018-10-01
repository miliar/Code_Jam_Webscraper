#!/usr/bin/env python
# encoding: utf-8
"""
googlerese.py

Created by Bill Soistmann on 2012-04-14.
for Google Code Jam 2012 Qaulifying A
"""
infile = 'A-small-attempt1.in'

replacements = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

cases = [line[:-1] for line in open(infile).readlines()]

for i,case in enumerate(cases):
	if i>0: print "Case #%s: %s" % (i,''.join(map(replacements.get,case)))
