#!/bin/env python

import GCJ

def GCD(x,y):
 return x if y == 0 else GCD(y,x-(y*(x/y)))

def solve(l):
 n = map(lambda x: int(x), l)
 n.pop(0)
 n.sort()
 n.reverse()
 gcd = 0
 cur = n[0]
 for i in n:
  gcd = GCD(gcd,cur-i)
  cur = i
 return str(-cur + (gcd * ((cur / gcd) + (1 if cur % gcd > 0 else 0))))

if __name__ == '__main__':
 GCJ.run(solve)
