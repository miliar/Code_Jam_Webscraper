
import sys
from math import sqrt, ceil, floor

def isPalindrome(s):
   l = len(s)
   i = 0
   j = -1
   while s[i] == s[j] and i < l + j:
      i += 1
      j -= 1
   return not (i < l + j)

def numFairSquare(a,b):
   count = 0
   lower = ceil(sqrt(a))
   upper = floor(sqrt(b))
   for i in xrange(int(lower), int(upper+1)):
      if isPalindrome(str(i)) and isPalindrome(str(i*i)):
         count += 1
         print >> sys.stderr, '%d --> %d' % (i, i*i)
   return count

def main():
   N = int(raw_input().strip())
   for t in xrange(N):
      (a,b) = raw_input().strip().split()
      print 'Case #%d: %d' % (t+1, numFairSquare(int(a),int(b)))

if __name__ == '__main__':
   main()
