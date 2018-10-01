#!/bin/python
import os, sys

filename = "B-small-attempt0"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")
T = int(infile.readline())
for index in xrange(T):
  items = infile.readline().split()
  C = int(items[0])
  bases = items[1:C+1]
  D = int(items[C+1])
  opposed = items[C+2:C+2+D]
  N = int(items[C+2+D])
  elems = items[C+2+D+1]
  
  print bases
  print opposed
  print elems
  
  # Create opposed map
  oppmap = {}
  for o in opposed:
    oppmap[o[0]] = o[1]
    oppmap[o[1]] = o[0]
  
  # Create combining map
  basemap = {}
  for b in bases:
    basemap[b[0] + b[1]] = b[2]
    basemap[b[1] + b[0]] = b[2]
  
  # Start invoking elements
  elemlist = []
  for e in elems:
    elemlist.append(e)
    
    # Check for combining elements
    c = basemap.get(''.join(elemlist[-2:]))
    if c:
      elemlist[-2:] = c
    # Check for opposing elements
    elif oppmap.get(e) in elemlist:
      elemlist = []
  
  outfile.write("Case #%d: [%s]\n" % (index+1, ', '.join(elemlist)))