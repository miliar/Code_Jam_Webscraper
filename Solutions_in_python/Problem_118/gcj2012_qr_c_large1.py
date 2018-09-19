import math


def isP2(s, n,m):
  if m < n:
    return True
  elif s[n] == s[m]:
    return isP2(s,n+1,m-1)
  else:
    return False

def isP(n):
 s = str(n)
 return isP2(s, 0, len(s)-1)

n = 1
ib = 100000000
while n < ib:
  if isP(n) and isP(n*n):
    print n
  n += 1
