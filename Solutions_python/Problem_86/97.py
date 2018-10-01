import sys, re
import fractions

cases = sys.stdin.readline()



for case in range(0,int(cases)):
  N,L,H = [int(x) for x in sys.stdin.readline().split()]
  PL = [int(x) for x in sys.stdin.readline().split()]
  res=1

  ok = False

  for i in range(L,H+1):
    if ok: break
    okk = True
    for p in PL:
      if not (i%p==0 or p%i==0):
        okk = False
    if okk:
      ok =True
      print "Case #%d: %d" % (case+1, i)
      break
  
  if not ok:
   print "Case #%d: NO" % (case+1)

