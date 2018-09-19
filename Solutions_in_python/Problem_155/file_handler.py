#!/usr/bin/python

def readfile(file):
  with open(file, "r") as f:
    nbCases = int(f.readline())
    cases = list()
    for case in range(nbCases):
      cases.append([int(x) for x in f.readline().split()[1]])
    return cases

def writesoluce(file, solucs):
  with open(file, "w") as f:
    for i in range(len(solucs)):
      f.write("Case #{}: {}\n".format((i + 1), solucs[i]))
