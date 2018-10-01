from fractions import gcd

t=int(input())

def ispower(n):
  while(n%2==0):
    n=n/2
  if(n==1):
    return(True)
  else:
    return(False)

def answer(n,d):
  ans=0
  while(n<d):
    d=d/2
    ans+=1
  return(ans)

for case in range(1,t+1):
  (n,d)=map(int,input().split('/'))
  g=gcd(n,d)
  n=int(n/g)
  d=int(d/g)
  if(ispower(d)):
    ans=answer(n,d)
    print("Case #"+str(case)+": "+str(ans))
  else:
    print("Case #"+str(case)+": impossible")
