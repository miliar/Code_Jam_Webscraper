#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(input())
def readfloat(): return float(input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, input().split())

def rev(v):
  if v == '+': return '-'
  return '+'

def flip(pancakes, pos, K):
  for i in range(K):
    pancakes[pos + i] = rev(pancakes[pos + i])

def solved(pancakes):
  return '-' not in pancakes

def solve(pancakes, K):
  
  count = 0
  for i in range(0, len(pancakes) - K + 1):
    if pancakes[i] == '-':
      flip(pancakes, i, K)
      count += 1
  
  if not solved(pancakes): return 'IMPOSSIBLE'
  
  return str(count)
  
if __name__ == '__main__':

  T = readint()
  for t in range(1, T+1):
    pancakes, K = input().split()
    pancakes = list(pancakes)
    K = int(K)
    ans = solve(pancakes, K)
    print('Case #%d: %s' % (t, ans))