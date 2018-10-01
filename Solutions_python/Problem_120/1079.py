#!/usr/bin/python

import math
import string

def main():
  cases = raw_input()
  cases = int(cases)
  i = 1
  while i <= cases:
    r_t = raw_input()
    r_t = string.split(r_t, ' ')
    r = int(r_t[0])
    t = int(r_t[1])
    s = math.pow((math.pow((2 * r - 1), 2) + 8 * t), 0.5)
    s = s - 2 * r + 1
    s /= 4.0
    res = s // 1
    print "Case #%d: %d" % (i, res)
    i += 1

if __name__ == '__main__':
  main()
