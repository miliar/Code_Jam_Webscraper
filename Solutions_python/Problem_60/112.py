#!/usr/bin/python
import sys,math

f = open(sys.argv[1],'r')
n = int(f.readline())
for tc in range(1,n+1):
  line=f.readline().rstrip('\n').split(" ")
  N=int(line[0])
  K=int(line[1])
  B=int(line[2])
  T=int(line[3])
  X=map(lambda x: int(x),f.readline().rstrip('\n').split(" "))
  V=map(lambda x: int(x),f.readline().rstrip('\n').split(" "))
  C=[]
  Q=[]
#  print K
  for i in range(N):
    C.append(int(math.ceil(float(B-X[i])/V[i])))
    Q.append(T*V[i]+X[i]-B)
#  print Q
  Result=0
  for c in range(N-1,N-K-1,-1):
    i=1
#    print "%d %d %d"%(c,Q[c],K)
    if Q[c]<0:
      i=c
#      print Q
#      print "issue ",
      while i>=0 and Q[i]<0:
        i=i-1
      if i>=0:
        for q in range(i,c):
          temp=Q[q]
          Q[q]=Q[q+1]
          Q[q+1]=temp
          Result=Result+1
#      print ""
      if (i<0):
        break
      else:
        K=K-1
    else:
      K=K-1
#  print Q
  if K!=0:
    Result="IMPOSSIBLE"
  print "Case #%d: %s"%(tc,Result)
