L, D, N = map(int, raw_input().split(' '))
master = {}
for _ in range(D):
  m = raw_input()
  p = master
  for c in m:
    if c not in p:
      p[c] = {}
    p = p[c]

#raw_input(master)
n = 0
def gen_candidates(atest, p, m):
  if p==len(atest):
    global n
    n+=1
  elif atest[p]=='(':
    for c in atest[p+1:atest.find(')',p)]:
      if c in m:
        gen_candidates(atest, atest.find(')',p)+1, m[c])
  else:
    c = atest[p]
    if c in m:
      gen_candidates(atest, p+1, m[c])
    
for _ in range(N):
  atest = raw_input()
  n = 0
  gen_candidates(atest, 0, master)
  print 'Case #%d: %d' % (_+1, n)
