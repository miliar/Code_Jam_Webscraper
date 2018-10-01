from itertools import ifilter

s = sorted

def war1(n, k):
  # original
  pts = 0
  while len(n) > 0:
    ke = k.pop(0)
    ne = next(ifilter(lambda x: x[1] > ke, enumerate(n)), None)
    if ne is None:
      n.pop(0)
    else:
      pts += 1
      n.pop(ne[0])
  return pts

def war2(n, k):
  # smarter
  pts = 0
  while len(n) > 0:
    ne = n.pop(0)
    ke = next(ifilter(lambda x: x[1] > ne, enumerate(k)), None)
    if ke is None:
      pts += 1
      k.pop(0)
    else:
      k.pop(ke[0])
  return pts

if __name__ == '__main__':
  import sys
  if len(sys.argv) > 1 and sys.argv[1] == 'tests':
    assert war1([0.5], [0.6]) == 0
    print war2([0.5], [0.6])
    assert war2([0.5], [0.6]) == 0
    print war1(s([0.7,0.2]), s([0.8,0.3]))
    assert war1(s([0.7,0.2]), s([0.8,0.3])) == 1
    assert war2(s([0.7,0.2]), s([0.8,0.3])) == 0
    assert war1(s([0.5, 0.1, 0.9]), s([0.6, 0.4, 0.3])) == 2
    print war2(s([0.5, 0.1, 0.9]), s([0.6, 0.4, 0.3]))
    assert war2(s([0.5, 0.1, 0.9]), s([0.6, 0.4, 0.3])) == 1
    assert war1(s([0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]), s([0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458])) == 8
    assert war2(s([0.186, 0.389, 0.907, 0.832, 0.959, 0.557, 0.300, 0.992, 0.899]), s([0.916, 0.728, 0.271, 0.520, 0.700, 0.521, 0.215, 0.341, 0.458])) == 4
  else:
    for t in range(int(raw_input())):
      e = int(raw_input())
      n = s(map(float, raw_input().split()))
      k = s(map(float, raw_input().split()))
      print 'Case #%d: %d %d' % (t+1, war1(n[:],k[:]), war2(n[:],k[:]))
      
