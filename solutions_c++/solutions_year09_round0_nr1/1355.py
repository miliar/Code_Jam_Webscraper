import re

L,D,N = map(int,raw_input().split())

words = [raw_input().strip() for i in range(D)]

pats = []
for i in range(N):
  pat = raw_input().strip()
  pat = pat.replace('(','[').replace(')',']')
  pat = re.compile(pat)

  ans = 0
  for j,word in enumerate(words):
    if pat.match(word) is not None:
      ans += 1

  print 'Case #%d: %d' % (i+1,ans)
