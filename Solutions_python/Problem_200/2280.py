def tidy(n):
  while n > 0:
    r = n % 10
    n //= 10
    if r < n % 10: return False

  return True

def last_tidy(N):
  return next(filter(tidy, reversed(range(N + 1))))

def smart_last_tidy(N):
  if tidy(N): return N
  return smart_last_tidy((N // 10 - 1)) * 10 + 9

if __name__ == '__main__':
  assert tidy(8)
  assert tidy(123)
  assert tidy(555)
  assert tidy(224488)
  assert not tidy(20)
  assert not tidy(321)
  assert not tidy(495)
  assert not tidy(999990)

  import sys

  T = int(sys.stdin.readline())
  for i in range(1, T + 1):
    N = int(sys.stdin.readline())
    #print('Case #{}: {}'.format(i, last_tidy(N)))
    print('Case #{}: {}'.format(i, smart_last_tidy(N)))
