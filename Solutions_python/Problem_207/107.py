for t in range(int(input())):
  n, r, o, y, g, b, v = (int(i) for i in input().split())
  if r == g and o == y == b == v == 0:
    result = "RG" * r
  elif y == v and r == o == g == b == 0:
    result = "YV" * y
  elif o == b and r == y == g == v == 0:
    result = "OB" * o
  elif r == g != 0 or y == v != 0 or o == b != 0:
    result = "IMPOSSIBLE"
  else:
    nr = r - g
    ny = y - v
    nb = b - o
    sort = sorted((("R", nr), ("Y", ny), ("B", nb)), key = lambda x: x[1])
    if sort[2][1] <= sort[1][1] + sort[0][1]:
      result = (sort[2][0] + sort[1][0] + sort[0][0]) * (sort[1][1] + sort[0][1] - sort[2][1]) + \
               (sort[2][0] + sort[1][0]) * (sort[2][1] - sort[0][1]) + \
               (sort[2][0] + sort[0][0]) * (sort[2][1] - sort[1][1])
      if g:
        result = result.replace("R", "R" + "GR" * g, 1)
      if v:
        result = result.replace("Y", "Y" + "VY" * v, 1)
      if o:
        result = result.replace("B", "B" + "OB" * o, 1)
    else:
      result = "IMPOSSIBLE"
  print("Case #%d: %s" % (t + 1, result))
  