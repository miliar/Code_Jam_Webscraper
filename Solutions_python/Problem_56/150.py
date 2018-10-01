#!/usr/bin/python
from sys import stdin

def convert(data, N):
  for row in range(0, N):
    for col in range(0, N):
      if data[row][col] == '.':
        data[row][col] = 0
      elif data[row][col] == 'R':
        data[row][col] = 1
      else:
        data[row][col] = 2
def testHelper(data, row, col, N, K, xi, yi, ret):
  if ret == 3:
    return ret
  if col + xi*K > N:
    return 0
  if yi == 1 and row + yi*K > N:
    return 0
  if yi == -1 and row + yi*K < -1:
    return 0
  prod = 1
  i = 0
  while i < K:
    prod = prod * data[row+i*yi][col+i*xi]
    i = i + 1
  if prod == 1:
    return 1
  if prod == pow(2,K):
    return 2
  return 0

def test(data, row, col, N, K):
  ret = 0
  ret = ret | testHelper(data, row, col, N, K, 1, 0, ret)
  ret = ret | testHelper(data, row, col, N, K, 0, 1, ret)
  ret = ret | testHelper(data, row, col, N, K, 1, 1, ret)
  ret = ret | testHelper(data, row, col, N, K, 1, -1, ret)
  return ret
  
def testOld(data, row, col, N, K):
  ret = 0
  if N - K >= col:
    #test horiz
    if N - K >= col:
      prod = 1
      i = 0
      while i < K:
        prod = prod*data[row][col+i]
        i = i+1
      if prod == 1:
        ret = ret | 1
      elif prod == pow(2, K):
        ret = ret | 2
      if ret == 3:
        return ret

    if row >= K-1:
      #test upper diagonal
      prod = 1
      i = 0
      while i < K:
        print data[row-i][col-i]
        prod = prod*data[row-i][col-i]
        i = i+1
      print prod
      if prod == 1:
        ret = ret | 1
      elif prod == pow(2, K):
        ret = ret | 2
      if ret == 3:
        return ret

    if N - K >= row:
      #test vertical
      prod1 = 1
      #test lower diagonal
      prod2 = 1
      i = 0
      while i < K:
        prod1 = prod1 * data[row+i][col]
        prod2 = prod2 * data[row+i][col+i]
        i = i+1
      if prod1 == 1:
        ret = ret | 1
      elif prod1 == pow(2, K):
        ret = ret | 2
      if ret == 3:
        return ret

      if prod2 == 1:
        ret = ret | 1
      elif prod2 == pow(2, K):
        ret = ret | 2
      if ret == 3:
        return ret
  return ret
     

def p(data, N):
  for row in range(0,N):
    res=""
    for col in range(0,N):
      res+=`data[row][col]`
    print res
    
    
  
TTT = int(stdin.readline())
for ttt in range(1,TTT+1):
  N, K = map(int,stdin.readline().split())
  data = []
  for t in range(0, N):
    data.append([])
    for ch in stdin.readline()[:-1]:
      data[-1].append(ch)
  for row in range(0, N):
    cur = N-1
    col = N-1
    while col >= 0:
      if data[row][col] == ".":
        col = col -1
      else:
        data[row][cur] = data[row][col]
        if col != cur:
          data[row][col] = "."
        cur = cur - 1
        col = col - 1
  convert(data, N)
  red = 0
  blue = 0
  done = 0
  for row in range(0, N):
    for col in range(0, N):
      ret = test(data, row, col, N, K)
      if ret == 1:
        red = 1
      elif ret ==2:
        blue = 1
      elif ret == 3:
        red = 1
        blue =1
      #print "%d,%d,%d,%d,"%(row, col, red, blue)
      if red==1 and blue == 1:
        print "Case #%d: Both" % (ttt)
        done = 1
        break
    if done:
      break
  if done:
    continue
  if red == 1:
    print "Case #%d: Red" % (ttt)
  elif blue == 1:
    print "Case #%d: Blue" % (ttt)
  else:
    print "Case #%d: Neither" % (ttt)

