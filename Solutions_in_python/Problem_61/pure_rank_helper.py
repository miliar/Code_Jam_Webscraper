#!/usr/bin/python
from sys import stdin

def isPure(i, n):
  arr = []
  cur = 0
  while i:
    if i%2:
      arr.append(cur)
    cur = cur + 1
    i = i>>1
  while 1:
    if n == 1:
      return 1
    if n not in arr:
      return 0
    n = arr.index(n) + 1
    

  
res = []
res.append(0)
res.append(0)  

for n in range(2,26):
  count = 0
  i = 0
  limit = pow(2,n-2)
  while i < limit:
    j = i << 2
    j = j | (1<<n)
    count = (count + isPure(j, n)) % 100003
    i = i +1
  res.append(count)
  print res
print res
