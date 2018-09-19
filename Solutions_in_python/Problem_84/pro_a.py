#!/usr/bin/python

import sys
import math

def main():
  # Get T
  line = sys.stdin.readline().strip()
  t = int(line)

  for x in range(t):
    # Get R, C
    line = sys.stdin.readline()
    col = line.split(' ')
    r = int(col[0])
    c = int(col[1])

    # Get tiles
    tile = []
    white_count = 0
    blue_count  = 0
    for y in range(r):
      line = sys.stdin.readline().strip()
      tile.append(list(line))
      white_count += line.count(".")
      blue_count  += line.count("#")
    #print tile

    # Check first
    impossible = 0
    if blue_count % 4 > 0:
      impossible = 1

    for i in range(r - 1):
      if impossible == 1:
        break
      for j in range(c - 1):
        if tile[i][j] == "#":
          if tile[i][j + 1] == "#" and \
             tile[i + 1][j] == "#" and \
             tile[i + 1][j + 1] == "#":
            tile[i][j] = "/"
            tile[i][j + 1] = "\\"
            tile[i + 1][j] = "\\"
            tile[i + 1][j + 1] = "/"
          else:
            impossible = 1
            break

    # Result
    print "Case #" + str(x + 1) + ":"
    if impossible == 1:
      print "Impossible"
    else:
      for i in range(r):
        for j in range(c):
          #print tile[i][j],
          sys.stdout.write(tile[i][j])
        print

if __name__ == '__main__':
  main()
