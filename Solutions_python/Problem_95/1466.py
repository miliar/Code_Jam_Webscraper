#!/usr/bin/python -O

import sys
import os
from string import maketrans

def main(argv=None):

  if argv is None:
    argv = sys.argv

  try: 
    f = open(sys.argv[1], 'r')
  except IndexError as e:
    print "Please specify an input file"
    return 127
  except IOError as e:
    print "Could not read file!"
    return 127

  T = int(f.readline())
  t = 1
  a = "abcdefghijklmnopqrstuvwxyz"
  b = "ynficwlbkuomxsevzpdrjgthaq"
  table = maketrans(b,a)
  while t <= T:
    p = f.readline().strip().translate(table)
    print "Case #" + str(t) + ': ' + p
    t += 1
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
