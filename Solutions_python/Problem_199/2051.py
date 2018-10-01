# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

HAPPY = '+'
BLANK = '-'
flips = 0


def all_happy(cakes):
  for i in cakes:
    if not i:
      return False
  return True

def flip(cakes, i):
  j = i
  while i < j + size:
    cakes[i] = not cakes[i]
    i += 1

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  strinput, size = input().split(" ")
  cakes = []
  for j in strinput:
    if j == '+':
      cakes.append(True)
    else:
      cakes.append(False)
  size = int(size)
  for k in range(len(cakes) - size + 1):
    if not cakes[k]:
      flip(cakes, k)
      flips += 1
  if all_happy(cakes):
    print("Case #{}: {}".format(i, flips))
  else:
    print("Case #{}: IMPOSSIBLE".format(i))
  flips = 0
  # check out .format's specification for more formatting options
