def tidy(k):
  i = len(k) - 1 
  j = 0
  
  while i > 0:
    if k[i] < k[i-1]:
      return 0
    i -= 1

  return 1


with open('B-small-attempt0.in', 'r') as f:
  T = f.readline()
  case = 1
  for linha in f:
    N = int(linha)
    print N
    while N > 0:
      flag = 0
      s = str(N)
      i = 0
      k = [0]*len(s)
      
      for c in s:
        k[i] = int(c)
        i += 1

      if tidy(k):
        f2 = open('small.out', 'a')
        f2.write("Case #{}: {}\n".format(case, s))
        print "Case #{}: {}".format(case, s)
        case += 1
        break
      else:
        N -= 1

