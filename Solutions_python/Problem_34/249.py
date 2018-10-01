import sys

(l, d, n) = map(int,sys.stdin.readline().split())
words = [""]*d
for wordnum in range(d):
  words[wordnum] = sys.stdin.readline()[:-1]
for c in range(n):
  pattern = sys.stdin.readline()[:-1]
  i = 0
  g = 0
  valid = words
  while i < len(pattern):
    poss = []
    if pattern[i] == '(':
      i += 1
      while pattern[i] != ')':
        poss.append(pattern[i])
        i += 1
    else:
      poss.append(pattern[i])
    i += 1
    valid = filter(lambda word: word[g] in poss, valid)
    g += 1
  sol = len(valid)
  print "Case #%d: %d" % (c+1, sol)
