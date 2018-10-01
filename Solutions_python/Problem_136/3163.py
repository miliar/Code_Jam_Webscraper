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
		
		line = dat.readline()
		numbers = line.strip().split(' ')
		c = float(numbers[0])
		f = float(numbers[1])
		x = float(numbers[2])
		
		minimum = 999999
		new_minimum = x / 2
		time = 0
		income = 2
		
		while new_minimum < minimum:
			minimum = new_minimum
			time += c / income
			income += f
			new_minimum = time + x / income
		
		out.write("Case #{0}: {1:.7f}\n".format(i+1, minimum))
					
	return 0

if __name__ == '__main__':
	main()

