ttt = int(input())

W = []

def trie(L):
  SS = set()
  for slowo in L:
    for i in range(len(slowo)+1):
      SS.add(slowo[:i])
  return len(SS)

def podziel(x,L):
  if x==m:
    T = []
    wyn = 0
    for i in range(n):
      T.append([])
    for i in range(m):
      T[L[i]].append(S[i])
    for i in range(n):
      if len(T[i])==0:
        return
      wyn += trie(T[i])
    W.append(wyn)
    return
  for i in range(n):      
    podziel(x+1, L+[i])

for tti in range(ttt):
  print("Case #%d:" % (tti+1), end=" ")
  buf = input().split(" ")
  m = int(buf[0])
  n = int(buf[1])
  S = []
  for i in range(m):
    S.append(input())
  podziel(0,[])
  x = max(W)
  print(x, W.count(x))
  W = []