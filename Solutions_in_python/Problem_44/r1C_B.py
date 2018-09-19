#!/usr/bin/python

###############################################################################
#
# Google Code Jam 2009 - Round 1C : B
#
# Author: Andres Ayala
# email: killerrex@gmail.com
# License: GPL3
#
# Usage:
#    ./r1C_a.py "input_file"  > output_file
#
###############################################################################

from sys import argv
from math import sqrt
eps = 1e-12

def mean(L):
  N = len(L)
  r = [0.0, 0.0, 0.0]
  for k in xrange(N):
    Lk = L[k]
    for i in xrange(3):
      r[i]+=Lk[i]
  return [r[0]/N, r[1]/N, r[2]/N]
  

def get_cm(Rl, Vl):
  """ Return R,V of CM"""
  R = mean(Rl)
  V = mean(Vl)
  return (R,V)

def dot(p1, p2):
  return p1[0]*p2[0]+p1[1]*p2[1]+p1[2]*p2[2]
  
def find_closer(Rcm, Vcm):
  
  R2 = dot(Rcm,Rcm)
  V2 = dot(Vcm,Vcm)
  dp = dot(Rcm,Vcm)
  # The CM is not moving or going away!!!
  if (dp>=0):
    t = 0.0
    d = sqrt(R2)
  else:
    t = -dp/V2 # note dp>0 ==> V2>0
    d2 = R2-dp*dp/V2
    # Avoid rounding errors
    if d2<0:
      d=0
    else:
      d = sqrt(R2-dp*dp/V2)
  return t,d
  

def read_swarm(fd):
  
  N = int(fd.readline())
  Rl = N*[[0,0,0]]
  Vl = N*[[0,0,0]]
  for k in xrange(N):
    l = map(float,fd.readline().strip().split())
    Rl[k] = l[0:3]
    Vl[k] = l[3:6]
  return (Rl, Vl)
  

###############################################################################
def batch(name):
  """ Read the input and print the output :-D"""
  
  fd = open(name,"r")
  T = int(fd.readline())

  i=1
  for k in xrange(T):
    (Rl,Vl) = read_swarm(fd)
    (Rcm,Vcm) = get_cm(Rl, Vl)
    (t,d) = find_closer(Rcm, Vcm)
    print "Case #%d: %10.7f %10.7f" % (i, d, t)
    i +=1

  fd.close()



###############################################################################
if __name__ == '__main__':
  if len(argv)==2:
    batch(argv[1])
  else:
    print "Usage: ", argv[0], " input_file"

