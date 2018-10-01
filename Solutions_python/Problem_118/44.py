import sys
sys.stdin = open("all1.txt","r")
d = []
n = int(input())
for i in range(n):
  d.append(int(input()))
d.sort()

sys.stdin = open("C-large-2.in","r")
ff=open("C-large-out-2.txt","w")

t = int(input())
for tt in range(t):
  print(tt)
  ans = 0
  n,m=map(int,input().split())
  for i in d:
    if i>=n and i<=m:
      ans += 1
  print("Case #",tt+1,": ",ans,sep='',file=ff)
