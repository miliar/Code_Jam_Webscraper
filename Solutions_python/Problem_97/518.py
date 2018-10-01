import sys

def num_pairs(a, b):
  l = len(str(a))
  pairs = 0
  for n in range(a, b + 1):
    sn = str(n)
    ms = set()
    for i in range(l):
      m = int(sn[i:l] + sn[0:i])
      if a <= n < m <= b:
        ms.add(m)
    pairs += len(ms)
  return pairs

if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    t = int(f.readline())
    for j in range(1, t + 1):
      a, b = (int(i) for i in f.readline().split())
      x = num_pairs(a, b)
      print 'Case #%d: %d' % (j, x)
