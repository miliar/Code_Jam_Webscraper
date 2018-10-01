def istidy(s):
  for i in xrange(len(s) - 1):
    if int(s[i+1]) < int(s[i]):
      return False
  return True

def solve(s):
  if istidy(s):
    return s
  else:
    return solve(str(int(s)-1))

t = int(raw_input())
for i in xrange(1, t + 1):
  s = raw_input()  
  print "Case #{}: {}".format(i, solve(s))