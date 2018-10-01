#!/usr/bin/env python
# encoding: utf-8
"""
A.py

Created by Chengyin Liu on 2010-05-23.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	tot_case = int(raw_input())
	case = 1
	
	while case <= tot_case:
		print "Case #%i:" % case,
		case = case + 1
		
		n = int(raw_input())
		wires = []
		intersect = 0
		
		for i in range(0,n):
			rawin = raw_input().split(' ')
			wires.append([int(rawin[0]), int(rawin[1])])
			
		wires.sort(key=lambda wire: wire[0])
		
		for wireno in range(0,n):
			for prevwireno in range(0,wireno):
				if wires[wireno][1] < wires[prevwireno][1]:
					intersect = intersect + 1
		
		print intersect

if __name__ == '__main__':
	main()

