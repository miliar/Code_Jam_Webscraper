#!/usr/bin/env python

import sys

def prepare():
  plain   = 'q a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'
  encoded = 'z y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
  map = {}
  for (p,e) in zip(plain,encoded):
    assert e == ' ' or (e >= 'a' and e <= 'z')
    if e in map:
      assert map[e] == p
    map[e] = p
  assert len(map) == 27
  return map

def solve_one(inp):
  ret = []
  for e in inp.strip('\n'):
    ret.append(map[e])
  return ''.join(ret)

def solve(inp):
  ret = []
  T = int(inp[0])
  for i in xrange(T):
    ret.append('Case #%d: %s' % (i+1,solve_one(inp[i+1])))
  return '\n'.join(ret)

map = {}

def main():
  global map
  map = prepare()
  #open('.'.join([sys.argv[1].split('.')[0],'out']),'w').write(solve(open(sys.argv[1],'r').readlines()))
  print open('.'.join([sys.argv[1].split('.')[0],'out']),'r').read()

if __name__ == '__main__':
  main()
