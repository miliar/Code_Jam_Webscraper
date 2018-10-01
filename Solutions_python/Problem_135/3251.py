#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Dino <dino@Dracon>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	
	dat = open("ulaz.txt")
	out = open("izlaz.txt", 'w')
	cases = int(dat.readline())
	for i in range(cases):
		row = int(dat.readline())
		izlaz = 0
		rjesenje = 0
		set = []
		for j in range(4):
			line = dat.readline()
			if row == j+1:
				numbers = line.strip().split(' ')
				for n in numbers:
					set.append(n)
		row = int(dat.readline())
		for j in range(4):
			line = dat.readline()
			if row == j+1:
				numbers = line.strip().split(' ')
				for n in numbers:
					if n in set:
						izlaz += 1
						rjesenje = n
		if izlaz == 0:
			out.write("Case #{0}: Volunteer cheated!\n".format(i+1))
		elif izlaz == 1:
			out.write("Case #{0}: {1}\n".format(i+1, rjesenje))
		else:
			out.write("Case #{0}: Bad magician!\n".format(i+1))
					
	return 0

if __name__ == '__main__':
	main()

