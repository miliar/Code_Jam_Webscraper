#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import *
#from sets import *
import math
import sys

if __name__ == "__main__":
	t = int(input())
	for caseIdx in range(1,t+1):
		sm, string = input().split(' ')
		needed = 0
		standed = 0
		for i in range(0,int(sm)):
			s = int(string[i])
			if 0 == s and 0 == standed:
				needed = needed + 1
			else:
				standed = standed + s - 1
		print("Case #%d: %d" % (caseIdx, needed))
