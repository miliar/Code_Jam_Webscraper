import sys

sys.stdin = open("cj1b_2-in-small.txt")

def map_inner_split(f, xs, by=" "):
  return map(lambda x: map(f, x.split(by)), xs)

lines = map(lambda l: l.strip(), list(sys.stdin))
lines = map_inner_split(int, lines)
n = lines[0][0]

c = 1
for a,b,k in lines[1:]:
  wins = 0
  for i in xrange(0, a):
    for j in xrange(0, b):
      if i & j < k:
        wins += 1
  print "Case #%d: %s" % (c, wins)
  c += 1
  