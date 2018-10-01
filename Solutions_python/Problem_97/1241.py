#! /usr/bin/env python
# code.py (@DESC@)
# Maintainer: Matias Larre Borges <matias@larre-borges.com>
# Last Change: 2012 Apr 14

import sys

def rotate(seq, n):
  return seq[n:] + seq[:n]

def main():
  file = open(sys.argv[1])
  nb_cases = int(file.readline())
  nb_case = 1
  for i in range(nb_cases):
    numbers = file.readline().split(' ')
    A = int(numbers[0])
    B = int(numbers[1])
    found = 0
    tagged = []
    for n in range(A,B+1):
      if n in tagged:
        #sys.stdout.write(("Skipping %d\n" % n))
        continue
      pairs = []
      results = []
      for r in range(1,len(str(n))):
        m = int(rotate(str(n),r))
        if m in results:
          continue
        if (n < m) and (m <= B):
          candidate = ("%d:%d" % (n,m))
          if candidate not in pairs:
            found = found + 1
            results.append(m)
            pairs.append(candidate)
      if (len(results) == 1):
        tagged.append(results[0])
    sys.stdout.write(("Case #%d: %d\n" % (nb_case, found) ))
    nb_case += 1
    file.close

if __name__ == "__main__":
  main()

