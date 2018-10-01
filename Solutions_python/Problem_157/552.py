def mul(u, v):
  return [u[0] * v[0] - u[1] * v[1] - u[2] * v[2] - u[3] * v[3],
       u[0] * v[1] + u[1] * v[0] + u[2] * v[3] - u[3] * v[2],
       u[0] * v[2] - u[1] * v[3] + u[2] * v[0] + u[3] * v[1],
       u[0] * v[3] + u[1] * v[2] - u[2] * v[1] + u[3] * v[0]]       

def comp(u):
  if u[0] == 1:
    return u
  else:
    return [0, -u[1], -u[2], -u[3]]

D = {'1': [1, 0, 0, 0], 'i': [0, 1, 0, 0], 'j': [0, 0, 1, 0], 'k': [0, 0, 0, 1]}

def solve(S):
  # preprocess,
  isI = [] 
  ijSeg = []
  vi = D['1'][:]
  for i in range(len(S)):
    vi = mul(vi, D[S[i]])
    if vi == D['i']:
      isI.append(i)
      ijSeg.append(vi)

  # product of the entire string
  prod = vi[:]

  isK = []
  jkSeg = []
  vk = D['1'][:]
  n = len(S)
  for i in range(len(S)):
    k = n-1-i
    vk = mul(D[S[k]], vk)
    if vk == D['k']:
      isK.append(k)
      jkSeg.append(vk)

  for iidx in range(len(isI)):
    i = isI[iidx]
    for kidx in range(len(isK)):
      k = isK[kidx]
      if k <= i: continue
      vj = mul(comp(ijSeg[iidx]), mul(prod, comp(jkSeg[kidx])))
      if vj == D['j']:
 #         print S[:i+1], S[i+1:k], S[k:]
        return True
  return False

f = open('C-small-attempt6.in', 'r')
#f = open('test.in', 'r')
T = int(f.readline())
for i in range(T):
  L, X = map(int, f.readline().split())
  s = f.readline()[:-1] * X
  if solve(s): 
    print 'Case #%d: YES' % (i+1)
  else:
    print 'Case #%d: NO' % (i+1)
