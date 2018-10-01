change = lambda x: "GABRIEL" if x == 1 else "RICHARD"

def res(a, b, c):
  if (a == 1):
    return 1

  if (a == 2):
    if ((b * c) % 2 == 0):
      return 1
    return 0

  if (a == 3):
    if ((b * c) % 3 != 0):
      return 0
    if (b * c == 3):
      return 0
    if (b * c == 6):
      return 1
    if (b * c == 9):
      return 1
    if (b * c == 12):
      return 1

  if (a == 4):
    if ((b * c) % 4 != 0):
      return 0
    if (b * c == 4):
      return 0
    if (b * c == 8):
      return 0
    if (b * c == 12):
      return 1
    if (b * c == 16):
      return 1



t = int(raw_input())

for case in range(1, t+1):
  a, b, c = [int(x) for x in raw_input().split()]
  print "Case #%d: %s" % (case, change(res(a, b, c)))
