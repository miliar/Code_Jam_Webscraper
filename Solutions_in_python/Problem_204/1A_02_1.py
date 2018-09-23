from math import ceil

def get(N,P,R,Q):
  #print(N,P)
  #print(R)
  #print(Q)
  ret = 0
  taken = dict()
  poidsset = set()
  for i in range(N):
    taken[i] = []
  candidates = dict()
  for i in range(N):
    candidates[i] = dict()
    sample = R[i]
    row = Q[i]
    for j,q in enumerate(row):
      sup = int((10*q)/(9*sample))
      inf = ceil((10*q)/(11*sample))
      for k in range(inf,sup+1):
        poidsset.add(k)
        if k in candidates[i]:
          candidates[i][k].append((j,sup))
        else:
          candidates[i][k] = [(j,sup)]
  li = ([max(candidates[i]) if candidates[i] else 0 for i in range(N)])
  m = max(li)
  poidslist = sorted(list(poidsset))
  for poids in poidslist:
    temp = dict()
    doit = True
    for i in range(N):
      if poids in candidates[i]:
        temp[i] = []
        for jsup in candidates[i][poids]:
          if jsup not in taken[i]:
            temp[i].append(jsup)
        if not temp[i]:
          doit = False
          break
      else:
        doit = False
        break
    if doit:
      n = min([len(temp[i]) for i in range(N)])
      ret += n
      for i in range(N):
        sol = dict()
        for jsup in candidates[i][poids]:
          j,sup = jsup
          if sup in sol:
            sol[sup].append(jsup)
          else:
            sol[sup] = [jsup]
        getn = 0
        for k in sorted(sol):
          if len(sol[k]) >= n-getn:
            for ik in range(n-getn):
              taken[i].append(sol[k][ik])
            break
          else:
            getn += len(sol[k])
            for solik in sol[k]:
              taken[i].append(solik)
      for i in range(N):
        candidates[i] = dict()
        sample = R[i]
        row = Q[i]
        for j,q in enumerate(row):
          sup = int((10*q)/(9*sample))
          inf = ceil((10*q)/(11*sample))
          jsup = (j,sup)
          if jsup not in taken[i]:
            for k in range(inf,sup+1):
              poidsset.add(k)
              if k in candidates[i]:
                candidates[i][k].append(jsup)
              else:
                candidates[i][k] = [jsup]
  return ret

T = int(input())

for i in range(1,T+1):
  N,P = map(int,input().split())
  R = list(map(int,input().split()))
  Q = []
  for j in range(N):
    Q.append(list(map(int,input().split())))
  ans = get(N,P,R,Q)
  print('Case #{}: {}'.format(i,ans))
