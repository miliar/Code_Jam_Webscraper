for i in range(input()):
   n,m=raw_input().split()
   m=list(map(int,list(m)))
   j=1
   a=0
   tmp=m[0]
   while(j<len(m)):
       if(tmp<j and m[j]>0):
           c=j-tmp
           a+= c
           tmp+=a
       tmp+=m[j]
       j+=1
   print("Case #%d: %d"%(i+1,a))   
