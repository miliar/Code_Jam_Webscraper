#!/usr/bin/python

###############################################################################
#
# Google Code Jam 2009 - Qualification Round C
#
# Author: Andres Ayala
# email: killerrex@gmail.com
# License: GPL3
#
# Usage:
#   > qual_b.py input_file
#
#   input_file: File with the format specificated in the problem
#               No sanity checks are done over this files
#
###############################################################################

from sys import argv

Welcome = "welcome to code jam"
N = len(Welcome)

def getnxt(txt, opt, k):
  """
  Return a
  """
  res = []
  if k==0:
    nxt = 0
  else:
    nxt = opt[k-1]
  l = Welcome[k]
  
  while nxt != -1:
    nxt = txt.find(l, nxt)
    if nxt!=-1:
      n = list(opt) # Make a copy!!
      n[k] = nxt
      res.append(n)
      nxt+=1
  return res
  

def say_welcome(txt):
  """
  Search for the number of combinations by brute force
  """

  opt = [ len(Welcome)*[0] ]

  for k in xrange(0, len(Welcome)):
    nxt = reduce(lambda x,y: x+y, [ getnxt(txt, tst, k) for tst in opt ])
    # Remove the empty ones
    opt = [ n[:] for n in nxt if len(n)>0 ]
    if len(opt)==0:
      break
  
  return len(opt)


def readsample(fName):
  
  fd = open(fName,"r")
  
  N = int(fd.readline().strip('\n'))
  
  k = 1
  for line in fd:
    Nop = say_welcome(line)
    print "Case #%d: %04d" % (k,Nop % 10000)
    k+=1

  fd.close()

###############################################################################
if __name__ == '__main__':
  
  if len(argv)==2:
    readsample(argv[1])
    
  else:
    print 'Usage: ' + argv[0] + ' input_file\n'

