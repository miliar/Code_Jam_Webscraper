def c(s):
  m = s/3
  if s%3 == 0:
    return max((m,m,m))
  if s%3 == 1:
    return max((m,m,m+1))
  if s%3 == 2:
    return max((m,m+1,m+1))
    
def cs(s):
  if s == 0 or s == 1:
    return -1
  m = s/3
  if s%3 == 0:
    return max((m-1,m,m+1))
  if s%3 == 1:
    return max((m,m,m-2))
  if s%3 == 2:
    return max((m,m,m+2))

def getMax(l, p, s):
  ss = 0
  cl = [c(x) for x in l]
  csl = [cs(x) for x in l]
  
  count = 0
  for t in zip(cl,csl):
    if t[0] >= p:
      count += 1
    elif t[1] >= p and ss < s:
      count += 1
      ss += 1
  
  return count
  
import sys
f = sys.stdin
num_of_lines = int(f.readline())

for i in range(num_of_lines):
  tokens = [int(x) for x in f.readline().split()]
  print "Case #%d: %s" % (i+1, getMax(tokens[3:], tokens[2], tokens[1]))

