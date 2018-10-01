import sys 
import string
from math import *
def isPalindrome(i):
  st = str(int(i))
  if len(st) == 1:
   #print sq
   return True
  for i in range (0, len(st)):
    if st[i] != st[len(st)-i-1]:
      return False 
  #print sq
  return True
f = open(sys.argv[1])

T = int(f.readline())
for i in xrange(0, T):
  line = f.readline().split(' ')
  #print line
  bottomsqrt = ceil(sqrt(int(line[0])))
  topsqrt = floor(sqrt(int(line[1].strip())))
  #print bottomsqrt
  #print topsqrt
  count = 0
  for j in range(int(bottomsqrt), int(topsqrt)+1):
   if isPalindrome(j):
    if isPalindrome(int(pow(j, 2))):
      count+=1
  print ''.join(('Case #', (str(i+1)), ':')), count


