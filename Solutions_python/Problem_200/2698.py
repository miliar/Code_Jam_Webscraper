t=int(input())
for k in range(t):
  s=input().strip()
  s=[int(e) for e in s]
  for i in range(len(s)-1,0,-1):
    if s[i]<s[i-1]:
      s[i-1]-=1 
      for j in range(i,len(s)):
        if s[j]==9:break
        s[j]=9
  d=0
  while(s[d]==0):d+=1 
  print("Case #"+str(k+1)+":","".join(map(str,s[d:])))