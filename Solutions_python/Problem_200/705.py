def break_integer(n):
  if n < 10:
    return [n]
  r = []
  while n:
    n, x = divmod(n, 10)
    r.insert(0, x)
  return r

def minus_one(n, p):
  while p >= 0:
    n[p] -= 1
    if n[p] >= 0:
      break
    n[p] += 10
    p -= 1

def eval_integer(n):
  r = 0
  for x in n:
    r = 10 * r + x
  return r

def tidy(n):
  n = break_integer(n)
  l = len(n)
  for i in xrange(l - 1, 0, -1):
    if n[i - 1] > n[i]:
      minus_one(n, i - 1)
      for j in xrange(i, l):
        n[j] = 9
  return eval_integer(n)


def solve(name):
  f = open(name, 'r')
  c = int(f.readline())
  for i in xrange(c):
    n = int(f.readline())
    print 'Case #%d: %d' % (i + 1, tidy(n))
  f.close()

def main():
  solve('B-large.in.txt')

if __name__ == '__main__':
  main()
