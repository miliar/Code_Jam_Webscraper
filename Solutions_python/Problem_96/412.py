#!/usr/bin/env python

import sys

def solve_one(inpu):
  inp = map(int, inpu.split())
  N,S,p = inp[:3]
  inp = inp[3:]
  ret = 0
  for i in xrange(N):
    mod3 = inp[i] % 3
    div3 = inp[i] / 3
    if mod3 == 0:
      if div3 >= p:
        ret += 1
      elif S > 0 and div3 >= 1 and div3+1 >= p:
        ret += 1
        S -= 1
    elif mod3 == 1:
      if div3+1 >= p:
        ret += 1
    else:
      if div3+1 >= p:
        ret += 1
      elif S > 0 and div3+2 >= p:
        ret += 1
        S -= 1

  return ret

def solve(inp):
  ret = []
  T = int(inp[0])
  for i in xrange(T):
    ret.append('Case #%d: %d' % (i+1,solve_one(inp[i+1])))
  return '\n'.join(ret)

def main():
  #open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
