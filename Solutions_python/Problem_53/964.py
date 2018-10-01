finame='A-small-attempt0.in'
foname='ponyo_re1.txt'

fi=open(finame,'r')
fo=open(foname,'w')
fi.readline()
def mink(n):
   light=False
   count=0
   p=[]
   o=[]
   p.append(1)
   for i in range(n):
         p.append(0)
         o.append(0)
   while not light:
      count+=1
      for i in range (n): 
         if p[i]==1:
            if o[i]==1:
               o[i]=0
            else:
               o[i]=1
      for i in range (n):
         p[i+1]=p[i]*o[i]
      if p[n]==1:
         light=True
   return count
     
t=0         
for line in fi:
   t+=1
   line=line.strip()
   line=line.split(' ')
   n=int(line[0])
   k=int(line[1])
   if ((k+1)%(mink(n)+1)==0):
      light='ON'
   else:
      light='OFF'
   fo.write('Case #%d: %s\n'%(t,light))
fi.close()
fo.close()