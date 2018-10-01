for t in range(input()):
  n = input()
  beg, end = 0, n
  while beg < end:
    cen = (beg + end + 1) / 2
    snext = str(cen)
    for i in range(1, len(snext)):
      if snext[i-1] > snext[i]:
        snext = snext[:i] + snext[i-1] * (len(snext)-i)
        break
    if int(snext) <= n:
      beg = cen
    else:
      end = cen - 1
  print('Case #%d: %s' % (t+1, beg))

