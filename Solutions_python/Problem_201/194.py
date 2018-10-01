from lcj import*
with openw() as g:
 def f(n,o):
  n,o=int(n),int(o)
  d=n
  b=basea(o,2)[:0:-1]
  for i in b:
   d=d//2-(i&((d+1)%2))
  return'%i %i'%((d//2,d//2-1+d%2)if d>1 else (0,0))
 for l in lines('C'):
  case(g,f(*l.split(' ')))