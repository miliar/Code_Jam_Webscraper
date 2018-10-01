#!/usr/bin/python
  
def solve():
  C,F,X = map(float,f.pop(0).split())
  farm = 0
  time = 0
  while True:
    rate = 2+farm*F
    if X/rate<C/rate+X/(rate+F):
      return time+X/rate
    time += C/(2+farm*F) 
    farm += 1

infile=open("B-large.in",'r')
f=map(lambda x:x.strip(),infile.readlines())
infile.close()
T=int(f.pop(0))
for t in xrange(T):
  print "Case #" + str(t + 1) + ": " + '%.7f' % solve()