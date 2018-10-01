import sys
from itertools import permutations

def ReadInts():
  return list(map(int, raw_input().strip().split(' ')))

def Cross(a, b):
  for i in a:
    for j in b:
      yield (i, j)
    
def Print(mess):
  print mess
  print >> sys.stderr, mess

for T in xrange(1, input() + 1):
  digits = raw_input()
  for f in xrange(2):
    if f: digits = '0' + digits
    for s in permutations(sorted(digits)):
      s = ''.join(c for c in s)
      if int(s) > int(digits): break
    if int(s) > int(digits): break
  Print('Case #%d: %s' % (T, s))
