def ken_war(kens, naomi):
  winners = set(x for x in kens if x > naomi)
  return min(winners) if len(winners) > 0 else min(kens)

def war(N, K):
  nP = 0
  for n in N:
    k = ken_war(K, n)
    nP += int(k < n)
    K = list(set(K) - set([k]))
  return nP

def dwar(N, K):
  while 1:
    if len(N) <= 0:
      return 0

    nW = reduce(
        lambda a, b: a and b,
        map(lambda x: x[0] > x[1], zip(sorted(N), sorted(K)))
    )
    if nW:
      return len(N)
    else:
      N = set(N) - set([min(N)])
      K = set(K) - set([max(K)])

def parse(challenge):
  cases = int(challenge[0])
  assert(3*cases+1 == len(challenge))
  t = [
      (challenge[i*3+2].split(), challenge[i*3+3].split())
      for i in range(cases)
    ]
  for i, (N, K) in enumerate(t):
    print 'Case #%d: %d %d' % (i+1, dwar(N, K), war(N, K))

import fileinput
parse([line.strip() for line in fileinput.input()])
