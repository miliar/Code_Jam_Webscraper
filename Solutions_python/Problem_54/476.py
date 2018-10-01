#!/usr/bin/python

import sys

def gcd(a, b):
  if a < 0:
    a *= -1
  if b < 0:
    b *= -1
  if a < b:
    t = a
    a = b
    b = t

  while b != 0:
    t = b
    b = a % b
    a = t
  return a

def main(argc, argv):
  ifile = open(argv[1], 'r')

  case = 0
  ifile.readline()

  for line in ifile:
    case += 1
    ts = map(int, line.split())

    T = ts[1] - ts[2]
    if T < 0:
      T *= -1

    if ts[1] > ts[2]:
      oldest = ts[1]
    else:
      oldest = ts[2]

    for i in range(2,len(ts)-1):
      T = gcd(T, ts[i]-ts[i+1])
      if ts[i+1] > oldest:
        oldest = ts[i+1]

    y = T - (oldest % T)
    if y % T == 0:
      y = 0

    print 'Case #' + str(case) + ': ' + str(y)

if __name__ == "__main__":
  main(len(sys.argv), sys.argv)
