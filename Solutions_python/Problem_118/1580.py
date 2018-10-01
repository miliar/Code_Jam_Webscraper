#!/usr/bin/python2 -tt

import sys
import math
import bisect

epsilon = 0.000000001
def compare(a, b):
  return abs(a - b) < epsilon


fair_and_squares = []


def fillFairAndSquares(A, B):
  lower = int(math.sqrt(A))
  upper = int(math.sqrt(B+1))
  
  for i in range(lower, upper+1):
    if is_palindrome(i): 
      sq = i*i
      if is_palindrome(sq):
        fair_and_squares.append(sq)
  #print fair_and_squares
  #print map(int, map(math.sqrt, fair_and_squares))



def is_palindrome(b):
  a = str(b)
  return a == a[::-1]





def compute(A, B): 
  #print A, B
  #print bisect.bisect_left(fair_and_squares, A)
  #print bisect.bisect_right(fair_and_squares, B)
  return bisect.bisect_right(fair_and_squares, B) - bisect.bisect_left(fair_and_squares, A)




def main():
  f = open("C-large-1.in", 'rU')
  lines = f.readline()
  fillFairAndSquares(0, 10**14)
  
  output = open('output', 'w')
  for i in range(int(lines)):
    line = map(long, f.readline().split(" "))
    A = line.pop(0)
    B = line.pop(0)
    #A = 100
    #B = 500
    out = compute(A, B)
    #print out
    output.write("Case #" + str(i+1) + ': ' + str(out) + '\n')
    #sys.stdout.write("Case #" + str(i+1) + ": " + str(out) + '\n')
  f.close()
  output.close()
  
if __name__ == '__main__':
  main()

