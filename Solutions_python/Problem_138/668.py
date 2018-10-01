def main():
  t = int(input())
  for i in range(t):
    n = int(input())
    naomi = input()
    ken = input()
    nb = naomi.split()
    nb = [float(b) for b in nb]
    nb.sort()
    kb = ken.split()
    kb = [float(b) for b in kb]
    kb.sort()
    nbb = nb[:]
    kbb = kb[:]
    nl = len(nb)
    j = 0
    while j < nl:
      if nb[j] < kb[j]:
        del nb[0]
        del kb[len(kb)-1]
        j = j - 1
        nl = nl - 1
      j = j + 1
    dwar = len(nb)
    nl = len(nbb)
    kl = len(kbb)
    j = 0
    k = 0
    while j < nl:
      while k < kl:
        if kbb[k] > nbb[j]:
          del kbb[k]
          del nbb[j]
          j = j - 1
          n1 = nl - 1
          kl = kl - 1
          break
        k = k + 1
      j = j + 1
    war = len(nbb)
    print("Case #"+str(i+1)+":",dwar,war)


main()
