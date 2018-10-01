import sys, re

def read():
  return sys.stdin.readline().split()

def readi():
  return [ int(x) for x in read() ]

l, d, n = readi()

dict = []
for i in range(d):
  dict.append(read()[0])

for i in range(n):
  s = '^' + read()[0] + '$'
  s = s.replace('(', '[')
  s = s.replace(')', ']')
  r = re.compile(s)

  ans = 0
  for j in range(d):
    if r.match(dict[j]):
      ans += 1

  print "Case #{0}: {1}".format(i + 1, ans)

