#!/usr/bin/python
import sys

def calc(mat):
  N = len(mat)
  M = len(mat[0])
  for i in xrange(N):
    for j in xrange(M):
      for i1 in xrange(N):
        if mat[i1][j] > mat[i][j]:
          break
      else:
        continue
      for j1 in xrange(M):
        if mat[i][j1] > mat[i][j]:
          break
      else:
        continue
      return "NO"
  return "YES"

def main():
  h = file(sys.argv[1])
  n = int(h.readline())
  for j in xrange(1,n+1):
    M,N = [int(x) for x in h.readline().split(" ")]
    mat = []
    for i in xrange(M):
      mat.append([int(x) for x in h.readline().split(" ")])
    print "Case #%d: %s" % (j, calc(mat))

main()
