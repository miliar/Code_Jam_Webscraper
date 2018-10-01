import math
fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
global pali
pali = {}

def pp(i):
  global pali
  p = pali.get(i, None)
  if p == None:
    if str(i) == str(i)[::-1]:
      p = True
      pali[i]=True
    else:
      p = False
      pali[i]=False
  return p

n = int(fi.readline())
for nn in range(n):
  l = fi.readline().split()
  A = int(l[0])
  B = int(l[1])
  s = 0
  for i in range(A,B+1):
    if not pp(i):
      continue
    sq = math.sqrt(i)
    if sq==int(sq) and pp(int(sq)):
      s += 1
  fo.write('Case #%d: %d\n'%(nn+1, s))
  print 'Case #%d: %d'%(nn+1, s)