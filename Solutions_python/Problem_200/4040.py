for x in xrange(int(raw_input())):
  n=map(int,list(raw_input()))
  num=[0]+[n[0]]
  prev=num[1]
  for i in xrange(1,len(n)):
    if n[i]<prev:
      j=-1
      while -j>=1:
        if num[j]-1>=num[j-1]:
          num[j]-=1
          break
        num[j]=9
        j-=1
      num+=['9'*(len(n)-i)]
      break
    prev=n[i]
    num+=[n[i]]
  print "Case #"+str(x+1)+':',int(''.join(map(str,num)))

