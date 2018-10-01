#python 2.5
a=file('A-large.in').read().split('\n')
a.reverse()
b=a.pop().split(' ');c=[];d=[]
for l in range(len(b)): b[l]=int(b[l])
for m in range(b[1]): c.append(a.pop())
for n in range(b[2]): d.append(a.pop())
def parts(pattern):
 p=list(pattern);p.reverse();b=[]
 while len(p)!=0:
  o=p.pop()
  if o=='(':
   b.append('')
   while True:
    k=p.pop()
    if k!=')': b[-1]=b[-1]+k
    else: break
  else: b.append(o)
 return b
def test(pp):
 m=0;g=parts(pp)
 for x in c:
  for l in range(b[0]):
   if x[l] not in g[l]: break
   elif l==b[0]-1: m+=1
 return m
out=file('A-large.out','w+')
for l in range(1,len(d)+1):
 out.write('Case #'+str(l)+': '+str(test(d[l-1]))+'\n')
out.close()