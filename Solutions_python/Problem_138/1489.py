def minesweeper(tokens):
  token = iter(tokens)
  cases = int(next(token))
  for case in range(cases):
    blocks = int(next(token))
    naomi = sorted([float(next(token)) for i in range(blocks)])
    ken_d = sorted([float(next(token)) for i in range(blocks)])
    ken_w = ken_d[:]
    deceitful, war = 0, 0
    while naomi:
      if sys.flags.debug: print "naomi:", naomi
      if sys.flags.debug: print "ken_d:", ken_d
      if sys.flags.debug: print "ken_w:", ken_w
      n = naomi.pop(0)
      if n < ken_d[0]:
        k_d = ken_d.pop()
      else:
        k_d = ken_d.pop(0)
      for i, v in enumerate(ken_w):
        if v > n:
          k_w = ken_w.pop(i)
          break
      else:
        k_w = ken_w.pop(0)
      if sys.flags.debug: print "n:", n, "k_d:", k_d, "k_w:", k_w
      if n > k_d: deceitful += 1
      if n > k_w: war += 1
      if sys.flags.debug: print "deceitful:", deceitful, "war:", war
    yield case+1, deceitful, war

if __name__ == "__main__":
  import sys
  for case, deceitful, war in minesweeper(sys.stdin.read().split()):
    print("Case #%s: %s %s" % (case, deceitful, war))
