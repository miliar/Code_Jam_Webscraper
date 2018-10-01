#!/usr/bin/python
import sys
import string


def calcProfit(rkn, g):
  R = string.atoi(rkn[0])
  K = string.atoi(rkn[1])
  N = string.atoi(rkn[2])
  gg = [string.atoi(x) for x in g]

  profit = 0
  i = 0
  while i < R:
    a = 0
    j = 0
    while (a + gg[0]) <= K:
      a = a + gg[0]
      b = gg[0]
      del gg[0]
      gg.append(b)
      j = j + 1
      if j == N:
        break
    else:
      if j == 0:
        a = gg[0]
        b = gg[0]
        del gg[0]
        gg.append(b)
    i = i + 1
    profit = profit + a

  return profit



def main():
  inputFile = open(sys.argv[1])
  caseCount = string.atoi(inputFile.readline())
  caseNum = 1
  l = 1
  RKN = []

  for line in inputFile:
    if l%2 == 1:
      RKN = line.split()
      l = l + 1
      continue
    g = line.split()
    print ("Case #%s: %s" % (caseNum, calcProfit(RKN, g)))
    caseNum = caseNum + 1
    l = l + 1

def test():
  nrk = "100 10 1".split()
  g = "1".split()
  print calcProfit(nrk, g)

main()
#test()
