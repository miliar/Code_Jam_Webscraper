def count(cell):
  total = 0
  for row in cell:
    for c in row:
      total += c
  return total

for case in xrange(1, int(raw_input())+1):
  R = int(raw_input())
  mx = 105
  cell = [[0] * mx for _ in xrange(mx)]
  for i in xrange(R):
    x1, y1, x2, y2 = map(int, raw_input().split())
    for x in xrange(x1+1, x2+2):
      for y in xrange(y1+1, y2+2):
        cell[x][y] = 1
  time = 0
  while count(cell) > 0:
    newcell = [[0] * mx for _ in xrange(mx)]
    for i in xrange(1, mx):
      for j in xrange(1, mx):
        if cell[i][j] and (cell[i-1][j] or cell[i][j-1]) or not cell[i][j] and (cell[i-1][j] and cell[i][j-1]):
          newcell[i][j] = 1
        else:
          newcell[i][j] = 0
    cell = newcell
    time += 1

  print "Case #%d: %d" % (case, time)
