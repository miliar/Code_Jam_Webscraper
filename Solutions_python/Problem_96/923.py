#!/usr/bin/env python
# encoding: utf-8

import sys
import os


def main():
	testcases = sys.stdin.readline().strip()
	for testcase in range(int(testcases)):
	  approved = 0
	  case = sys.stdin.readline().strip().split()
	  surprises = int(case[1])
	  avarage = int(case[2])
	  points = case[3:]
	  
	  for score in points:
	    if int(score) == 0 and avarage != 0:
	      continue
	    
	    mean = int(score)/3
	    rest = int(score)%3
	    
	    if mean >= avarage:
	      approved += 1
	    elif rest >= 1 and mean + 1 >= avarage:
	      approved += 1
	    elif rest == 2 and mean + 2 >= avarage and surprises > 0:
	      approved += 1
	      surprises -= 1
	    elif mean + 1 >= avarage and surprises > 0:
	      approved += 1
	      surprises -= 1
	  sys.stdout.write("Case #%d: %d\n" % (testcase + 1, approved))


if __name__ == '__main__':
	sys.exit(main())

