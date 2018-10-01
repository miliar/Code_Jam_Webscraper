import sys

def unpack_list(a, b, c, *d):
  return a, b, c, d

def max_num(n, s, p, ts):
  at_least_p = 0
  not_surprising_minimum = max((p-1)*3 + 1, p)
  surprising_minimum = max((p-2)*3 + 2, p)
  
  for t in ts:
    if t >= not_surprising_minimum:
      at_least_p += 1
    elif t >= surprising_minimum and s > 0:
      at_least_p += 1
      s -= 1
      
  return at_least_p

if __name__ == '__main__':
  with open(sys.argv[1], 'r') as f:
    t = int(f.readline())
    for j in range(1, t + 1):
      n, s, p, ts = unpack_list(*(int(i) for i in f.readline().split()))
      y = max_num(n, s, p, ts)
      print 'Case #%d: %d' % (j, y)
