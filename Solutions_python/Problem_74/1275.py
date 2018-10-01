#!/usr/bin/env python
# encoding: utf-8
"""
input.py

Created by Sergio Nakanishi on 2011-05-06.
Copyright (c) 2011 Atama. All rights reserved.
"""

import sys
import os
import math
from collections import deque

def main():
	f = open('input.in', 'r')
	
	lines = deque([ line.strip() for line in f.readlines() ])
	
	f.close()
	
	T = int(lines.popleft())
	
	output = []
	current_case = 1
	for line in lines:
		tokens = deque(line.split(' '))
		N = int(tokens.popleft())
		O = 1
		B = 1
		last_robot = ''
		total_secs = 0
		secs_passed = 0
		while len(tokens) > 0:
			current_total_secs = 0
			current_robot = tokens.popleft()
			current_pos = 0
			if current_robot == 'O':
				current_pos = O
			else:
				current_pos = B
			target_pos = int(tokens.popleft())
			secs_to_move = math.fabs(current_pos - target_pos)
			current_total_secs = secs_to_move + 1
			if last_robot == current_robot:
				secs_passed += current_total_secs
			else:
				current_total_secs -= secs_passed
				if current_total_secs <= 0:
					current_total_secs = 1
				secs_passed = current_total_secs
			total_secs += current_total_secs
			
			last_robot = current_robot
			if current_robot == 'O':
				O = target_pos
			else:
				B = target_pos
			#print "current_total_secs = {0}, secs_passed = {1}".format(current_total_secs, secs_passed) 
		output.append("Case #{0}: {1}".format(current_case, int(total_secs)))
		current_case += 1
		
		f = open('output.txt', 'w')
		f.write("\n".join(output))
		f.close()

if __name__ == '__main__':
	main()

