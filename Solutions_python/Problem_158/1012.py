import math # floordiv

# Calculations, gud vet...
def omino(a, b, c, index):
  boolean = False

  if a > b and a > c:
    boolean = True
  elif (b * c) % a != 0:
    boolean = True
  elif (a + 1) // 2 > min(b, c):
    boolean = True
  elif a == 1 or a == 2 or a == 3:
    boolean = False
  elif a == 4:
    boolean = not(min(b, c) > 2)
  elif a == 5:
    boolean = min(b, c) == 3 and max(b, c) == 5
  elif a == 6:
    boolean = not(min(b, c) > 3)

  if boolean == True:
    return 'RICHARD'
  else:
    return 'GABRIEL'

# Input & Result
for case in range(0, int(input())):
  a, b, c = map(int, input().split(' '))
  print( "Case #%d: %s" % (case + 1, omino(a, b, c, case)) )