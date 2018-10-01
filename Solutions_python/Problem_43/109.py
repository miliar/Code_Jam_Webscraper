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

def main():
	with open("A-large.in") as f:
		n = f.readline()
		n = int(n)

		for case in xrange(1, n+1):
			st = f.readline().strip()
			numbers = list(st)
			voc = {}


			voc[numbers[0]] = 1
			if (len(numbers) > 1):
				pos = 1
				while pos < len(numbers) and numbers[pos] in voc:
					pos += 1
				if pos < len(numbers):
					voc[numbers[pos]] = 0
					value = 2
					while pos < len(numbers):
						while pos < len(numbers) and numbers[pos] in voc:
							pos += 1
						if pos < len(numbers):
							voc[numbers[pos]] = value
							value += 1

			base = len(voc)
			if base == 1:
				base += 1

			answer = 0
			level = 1
			numbers.reverse()

			for digit in numbers:
				answer += voc[digit] * level
				level *= base

			print "Case #%d: %d" % (case, answer)
	return 0

if __name__ == '__main__': main()
