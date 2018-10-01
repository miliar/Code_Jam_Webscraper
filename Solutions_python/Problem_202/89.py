#!/usr/bin/python

t=input()
for i in xrange(t):
  n,m=map(int,raw_input().strip().split())
  initmodels=[" "]*n
  score=0
  for j in xrange(m):
    t,r,c=raw_input().strip().split()
    initmodels[int(c)-1]=t
    if t=="o":
      score+=2
    else:
      score+=1
  newmodels=[]
  if "o" not in initmodels and "x" not in initmodels:
    newmodels.append("o 1 1")
    inito=0
    if initmodels[0]=="+":
      score+=1
    else:
      score+=2
  elif "x" in initmodels:
    xc=initmodels.index("x")
    newmodels.append("o 1 "+str(xc+1))
    inito=xc
    score+=1
  else: #"o" in initmodels:
    oc=initmodels.index("o")
    inito=oc
  for j in xrange(n):
    if j!=inito and initmodels[j]==" ":
      newmodels.append("+ 1 "+str(j+1))
      score+=1
  #if n==1 then we are done. Otherwise take care of the diagonals and
  #bottom row
  if n>2:
    #diagonal
    for k in xrange(1,n-1):
      if inito==n-1:
        col=n-k
      elif k<=inito:
        col=k
      else:
        col=k+1
      newmodels.append("x "+str(k+1)+" "+str(col))
      score+=1
    #bottom row +s
    for k in xrange(2,n):
      newmodels.append("+ "+str(n)+" "+str(k))
      score+=1
  if n>1:
    #bottom row x
    if inito==n-1:
      newmodels.append("x "+str(n)+" "+str(1))      
    else:
      newmodels.append("x "+str(n)+" "+str(n))
    score+=1
  print "Case #"+str(i+1)+": "+str(score)+" "+str(len(newmodels))
  for lin in newmodels:
    print lin
