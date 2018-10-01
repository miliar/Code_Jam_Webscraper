import itertools

T = int(raw_input())

for case in range(1, T+1):

  A, B, K = map(int, raw_input().split())

  a = tuple(range(A))
  b = tuple(range(B))

  prod = tuple(itertools.product(a, b, repeat=1))

  count = 0
  for p in prod:
    if p[0]&p[1] < K:
      count += 1

  print 'Case #' + str(case) + ': ' + str(count)
