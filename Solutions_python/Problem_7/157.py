#!/usr/bin/env python
# encoding: utf-8

import sys
import getopt


help_message = '''
The help message goes here.
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg


def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
  
    # option processing
    for option, value in opts:
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    print >> sys.stderr, "\t for help use --help"
    return 2
  
  
  lines = file(args[0]).read().splitlines()
  
  numCases = int(lines[0])
  
  for lineNum, line in enumerate(lines[1:]):
    n, A, B, C, D, x0, y0, M = map(int, line.split(' '))
    treesList = []
    triangles = 0
    x, y = x0, y0
    for i in xrange(n):
      treesList.append((x, y))
      x = (A*x + B) % M
      y = (C*y + D) % M
    
    for idx1 in xrange(n):
      z1x, z1y = treesList[idx1]
      for idx2 in xrange(idx1+1,n):
        z2x, z2y = treesList[idx2]
        for idx3 in xrange(idx2+1,n):
          z3x, z3y = treesList[idx3]
          
          if not (z1x + z2x + z3x) % 3 == 0:
            continue
          if not (z1y + z2y + z3y) % 3 == 0:
            continue
          
          triangles += 1
    
    print "Case #%i: %i" % (lineNum+1,triangles)




if __name__ == "__main__":
  sys.exit(main())
