from math import *
from itertools import *
import os

# general helper functions

def split_to_int(f):
    return [int(v) for v in f.next().split()]

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def isPrime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


# problem

def main():
    # f = open("/home/jackie/Documents/Codejam/in")
    # lines = f.readlines()
    # cases = int(lines.pop(0))
    # for i in range(cases):
    #     print "Case #%d:" % (i+1),

    with open("/Users/jackie/Dropbox (Personal)/Documents/Codejam/in.in") as f:
        cases = int(f.next())
        for i in range(cases):
            print "Case #%d:" % (i+1),
            possible = set()
            row = int(f.next())
            j = 1
            for k in range(4):
                line = f.next()
                if j == row:
                    possible = set(int(c) for c in line.split())
                j += 1

            possible2 = set()
            j = 1
            row = int(f.next())
            for k in range(4):
                line = f.next()
                if j == row:
                    possible2 = set(int(c) for c in line.split())
                j += 1

            same = possible & possible2
            if len(same) == 1:
                print list(same)[0]
            elif not same:
                print 'Volunteer cheated!'
            else:
                print 'Bad magician!'


main()
