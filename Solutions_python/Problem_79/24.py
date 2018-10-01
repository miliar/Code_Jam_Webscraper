def pattern(s,c): 
  pl=[(c if x==c else '_') for x in s]
  return ''.join(pl)
T=int(input())
for i in range(T):
  N,M=[int(x) for x in input().split()]
  di=[input() for j in range(N)]
  orders = [input() for j in range(M)]
  ans = []
  maxl = max([len(x) for x in di])
  for order in orders:
    value=[1]*N
    state=[[] for j in range(maxl+1)]
    for j in range(N):
      state[len(di[j])].append((di[j],j))
    for c in order:
      nstate=[]
      #print(state)
      for j in range(len(state)):
        d={}
        sj=state[j]
        if len(sj)<=1:
          continue
        for y in sj:
          p=pattern(y[0],c)
          if p not in d:
            d[p]=[]
          d[p].append(y)
        l = list(d.values())
        if len(l)>1:
          for (w,n) in sj:
            if c not in w:
              value[n] += 1
              #print(c,w,1)
        #elif c not in sj[0][0]:
          #for (w,n) in sj:
            #value[n] += 1
            #print(c,w,2)
        nstate.extend(l)
      state=nstate
    ans.append(di[min([(-value[j],j) for j in range(N)])[1]])
  print('Case #%d: ' % (i+1),end='')
  print(*ans)