import math
import sys
rl = lambda : sys.stdin.readline().strip()

def is_palindrome(num):
  numstr = str(num)
  l = 0
  u = len(numstr) - 1
  while l < u:
    if numstr[l] != numstr[u]:
      return False
    l += 1
    u -= 1
  return True

def main():
  cases = int(rl())
  for c in xrange(1, cases+1):
    l, u = map(long, rl().split())
    total = 0
    for i in range(l, u+1):
      if not is_palindrome(i):
        continue
      sq = math.sqrt(i)
      if not sq.is_integer():
        continue
      if not is_palindrome(int(sq)):
        continue
      total += 1
    print "Case #%d: %d" % (c, total)

main()
