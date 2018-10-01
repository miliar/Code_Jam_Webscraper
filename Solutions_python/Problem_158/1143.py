t = int(input())

for i in range(t):
  xrc = map(int, raw_input().split())
  X = xrc[0]
  R = xrc[1]
  C = xrc[2]

  if R > X - 2 and C > X - 2 and (R * C) % X == 0 and X < 7:
    print "Case #" + str(i + 1) + ": GABRIEL"
  else:
    print "Case #" + str(i + 1) + ": RICHARD"