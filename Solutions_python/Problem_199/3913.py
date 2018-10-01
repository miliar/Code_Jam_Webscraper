from sys import stdin

T = int(stdin.readline().strip())
pancakes, S, K = [], 0, 0

def flip(pos):
  for i in range(K):
    if pancakes[pos + i] == '+':
      pancakes[pos + i] = '-'
    else:
      pancakes[pos + i] = '+'

def happy(pos, flips):
  if pos > S - K:
    if pancakes[pos] == '-':
      return 'IMPOSSIBLE'
    if pos == S - 1:
      return flips
    return happy(pos + 1, flips)

  if pancakes[pos] == '+':
    return happy(pos + 1, flips)
  else:
    flip(pos)
    return happy(pos + 1, flips + 1)



for i in range(T):
  pancakes, K = stdin.readline().strip().split()
  pancakes = list(pancakes)
  S = len(pancakes)
  K = int(K)

  print("Case #{0}: {1}".format(i + 1, happy(0,0)))
