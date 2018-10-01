#!/usr/bin/python

import sys
import math

primes = []

def main():
  # Get T
  line = sys.stdin.readline().strip()
  t = int(line)

  for x in range(t):
    # Get N, L, H
    line = sys.stdin.readline().strip()
    col = line.split(' ')
    n = int(col[0])
    l = int(col[1])
    h = int(col[2])

    # Get notes by other players
    line = sys.stdin.readline().strip()
    note = line.split(' ')
    #print note

    result = 0
    for i in range(l, h + 1):
      ok = 1
      for j in range(n):
        if i % int(note[j]) == 0 or int(note[j]) % i == 0:
          continue
        else:
          ok = 0
          break
      if ok == 1:
        result = i
        break

    # Result
    if result == 0:
      print "Case #" + str(x + 1) + ": NO"
    else:
      print "Case #" + str(x + 1) + ": " + str(result)

if __name__ == '__main__':
  main()
