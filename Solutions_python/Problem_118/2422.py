import numpy as nm
def pal(k):
  return str(k)==str(k)[::-1]
def fair(k,ln):
  t=0
  l = nm.unique(nm.sqrt(k).astype(int))
  for n in l:
   if pal(n) and pal(n*n) and n*n in k:
    t=t+1
  print "Case #%s: %s"%(int(ln)+1,t)
fl=open("ques")
no=int(fl.readline())
for ln in range(0,no):
 tt=fl.readline()
 ls=tt.split()
 fair(nm.arange(int(ls[0]),int(ls[1])+1),ln)
