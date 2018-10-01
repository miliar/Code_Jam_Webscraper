from functools import reduce

def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
  return (a // gcd(a, b)) * b

for case in range(1, int(input()) + 1):
  N, L, H = map(int, input().split())
  notes = sorted(int(n) for n in input().split())
  notes = [reduce(lcm, notes, 1)] + notes

  note = 'NO'
  for n in range(L, H+1):
    if all(not n % m or not m % n for m in notes):
      note = n
      break

  print('Case #%d: %s' % (case, note))
