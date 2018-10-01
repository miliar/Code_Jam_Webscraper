# -*- coding: utf-8 -*-
import sys

def ReadInts(f):
  buf = f.readline().rstrip("\n").split()
  return map(int,buf)

def highers(totals,p,S):
  ret = 0
  for total in totals:
    if total == 0:
      if p == 0:
        ret += 1
      continue

    if total % 3 == 0:
      maximum = total/3
      if maximum >= p:
        ret += 1
      elif (maximum+1) >= p and S > 0:
        ret += 1
        S -= 1
    elif total % 3 == 1:
      maximum = total/3 + 1
      if maximum >= p:
        ret += 1
    else:
      maximum = total/3 + 1
      if maximum >= p:
        ret += 1
      elif (maximum+1) >= p and S > 0:
        ret += 1
        S -= 1
  return ret

def main():
  T = ReadInts(sys.stdin)[0]
  for prob in xrange(1,T+1):
    inputs = ReadInts(sys.stdin)
    N = inputs[0]
    S = inputs[1]
    p = inputs[2]
    totals = inputs[3:]
    
    ret = highers(totals,p,S)
    print "Case #%d: %d"%(prob,ret)

if __name__ == "__main__":
  main()
  
  
