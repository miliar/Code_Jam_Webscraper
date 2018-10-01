#!/usr/bin/python

import sys

def main(argc, argv):
  ifile = open(argv[1], 'r')

  case_num = int(ifile.readline()[:-1])

  for case in range(1, case_num+1):
    N, K, B, T = map(int, ifile.readline().split())
    position = map(int, ifile.readline().split())
    velocity = map(int, ifile.readline().split())
    position.reverse()
    velocity.reverse()

    not_fast_enough = 0
    swaps = 0
    fast_enough = 0

    for i in range(0, len(position)):
      if (B-position[i]) > (velocity[i] * T):
        not_fast_enough += 1
      else:
        swaps += not_fast_enough
        fast_enough += 1

      if fast_enough >= K:
        break

    if fast_enough < K:
      swaps = "IMPOSSIBLE"

    print "Case #" + str(case) + ": " + str(swaps)

if __name__ == "__main__":
  main(len(sys.argv), sys.argv)
