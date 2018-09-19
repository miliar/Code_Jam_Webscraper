
corpus = [
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv','so it is okay if you want to just give up'),
    ]
TR = {'z':'q', 'q':'z',}

for bad, good in corpus:
  for bch, gch in zip(bad, good):
    if bch in TR:
      assert TR[bch] == gch
    TR[bch] = gch

#print ''.join(sorted(TR.keys()))

N = int(raw_input())
def translate(mapping, text):
  return ''.join(mapping[ch] for ch in text)

for i in range(N):
  print 'Case #%d:' % (i+1), translate(TR, raw_input())


