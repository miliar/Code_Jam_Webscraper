#!/usr/bin/python
import pdb, sys, math, bisect

debug = False
def dbg(line):
  if debug == True: print(line)

def compute(n, r, t):
  return 2*n*n + (2*r-1)*n - t

def get_result(r, t):
  a = 2
  b = 2*r - 1
  c = t
  tmp = b*b + 4*a*c
  nb = (-1 * b + math.sqrt(tmp) ) / 4;
  n = int(nb)
  while compute(n, r, t) > 0:
    n = n - 1
  return n

def main(f):
  fs = open(f, "r")
  lines = fs.readline()
  lines = int(lines)
  for l in xrange(lines):
    line = fs.readline()
    n, k = line.split()
    n = int(n); k = int(k)
    res = get_result(n, k)
    print("Case #{0}: {1}".format((l+1), res))

if __name__ == "__main__":
  main(sys.argv[1])
