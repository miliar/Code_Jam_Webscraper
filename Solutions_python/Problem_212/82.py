#!/usr/bin/python

t=input()
for i in xrange(t):
  n,p=map(int,raw_input().strip().split())
  g=map(int,raw_input().strip().split())
  mods=[0]*p
  for gi in g:
    mods[gi%p]+=1
  order=[0]*mods[0]
  if p==2:
    order+=[1]*mods[1]
  elif p==3:
    pairs=min(mods[1],mods[2])
    order+=[1,2]*pairs
    mods[1]-=pairs
    mods[2]-=pairs
    order+=[1]*mods[1]
    order+=[2]*mods[2]
  elif p==4:
    order+=[2,2]*int(mods[2]/2)
    mods[2]=mods[2]%2
    pairs=min(mods[1],mods[3])
    order+=[1,3]*pairs
    mods[1]-=pairs
    mods[3]-=pairs
    while mods[2]>=1 and mods[1]>=2:
      order+=[1,1,2]
      mods[1]-=2
      mods[2]-=1
    while mods[2]>=1 and mods[3]>=2:
      order+=[3,3,2]
      mods[3]-=2
      mods[3]-=1
    order+=[1]*mods[1]
    order+=[2]*mods[2]
    order+=[3]*mods[3]
  #count fresh groups
  used=0
  fresh=0
  for j in order:
    if used%p==0:
      fresh+=1
    used+=j
  print "Case #"+str(i+1)+": "+str(fresh)
