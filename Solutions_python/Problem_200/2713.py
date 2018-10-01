#!/usr/bin/python
# -*- coding: utf-8 -*-
import fileinput
import logging
import random
import itertools
import re
import math


logging.basicConfig(level=logging.DEBUG)


def find_answer(line):
  ''' Find the answer for this question '''
  s = line[0]
  result = ''
  m='9'
  sorteds = ''.join(sorted(s))
  while s and sorteds != s :
    # while s[-1] == sorteds[-1]:
    #   result = s[-1] + result 
    #   s = s[:-1]
    #   m = result
    # if s:
    result = m + result
    if m>s[-1]:
      ints = int(s[:-1]) - 1
      s = str(ints) if ints != 0 else '' 
    else:
      s = s[:-1]  
    sorteds = ''.join(sorted(s))
  result = s + result
  return result

case_lines = 1
def main():
  ''' Parse the input lines '''
  lines = [l.strip() for l in fileinput.input()]
  # Solve your problem here
  logging.debug(lines)
  n_tests = int(lines[0])
  start_test = 1 

  for i in xrange(0, n_tests):
    n_lines = case_lines if case_lines >0 else (int(lines[start_test]) + 1)
    tc = lines[start_test:start_test+n_lines]
    logging.debug(tc)
    n = find_answer(tc)
    # test(tc, n)
    print 'Case #{}: {}'.format(i+1, n)
    start_test += n_lines

if __name__ == '__main__':
  main()
