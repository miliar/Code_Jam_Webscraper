import sys,math

s=int(input())
s1=1
count=0
while s1<=s:
  count=0
  a=sys.stdin.readline()
  l=a.split()
  for i in range(int(l[0]),int(l[1])+1):
      if str(i)!=str(i)[::-1]:
            continue
      else:
         k=math.sqrt(i)
         if (k-int(k))!=0:
              continue
         else: 
              if str(int(k))!=str(int(k))[::-1]:
                       continue
              else:
                      count=count+1
  print 'Case #'+str(s1)+':'+' '+str(count) 
  s1=s1+1


