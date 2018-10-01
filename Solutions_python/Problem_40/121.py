#!/usr/bin/env python
#
#       jam.py
#
#       Copyright 2009 Denis <denis@denis-desktop>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import re

class node:
	parser = re.compile('^\s*\(\s*([0-9.]+)\s*([A-Za-z]*)(.*)')
	stripper = re.compile('^(\s*\))+')
	def __init__(self):
		self.weight = 1
		self.name = None
		self.good = None
		self.bad = None

	def fromSource(self, src, parent = None, type = None):
		#print 'src is ', src
		if (parent):
			if (type == 'good'):
				parent.good = self
			else:
				parent.bad = self
			src = self.stripper.sub('', src)

		match = self.parser.match(src)
		#if not match:
		#	print 'no match! src is ', src
		self.weight, self.name, next = match.groups()
		self.weight = float(self.weight)
		#print 'got weight name', self.weight, self.name
		if self.name:
			next = node().fromSource(next, self, 'good')
			next = node().fromSource(next, self, 'bad')
		return next

	def test(self, features, k = 1):
		k *= self.weight
		if self.name:
			if (self.name in features):
				return self.good.test(features, k)
			else:
				return self.bad.test(features, k)
		return k

def main():
	with open("A-large.in") as f:
		n = f.readline()
		n = int(n)

		for case in xrange(1, n+1):
			print "Case #%d:" % case

			treesrc = ''
			l = int(f.readline())
			for i in xrange(0, l):
				treesrc += f.readline()[:-1]
			tree = node()
			tree.fromSource(treesrc)

			a = int(f.readline())
			for i in xrange(0, a):
				features = f.readline().strip().split(' ')
				features = features[2:]
				print "%.7f" % tree.test(features)
	return 0

if __name__ == '__main__': main()
