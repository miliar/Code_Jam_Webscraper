# -*- coding: utf-8 -*-
from time import clock
from math import floor
from math import ceil



    
import sys
sys.setrecursionlimit(30000)

start1 = clock()


f=open('a.inp', 'r')
f1=open('a.out', 'w')
T=int(f.readline())
print (T)


for t in range (1,T+1):
    f1.write('Case #'+str(t)+':\n')
    st=f.readline()
   
   
    n=int(st.split(' ')[0])
  #  pd=int(st.split(' ')[1])
  #  pg=int(st.split(' ')[2])
    k=[]
    
    print('case ',t,n)
    for j in range (n):
        k1=[]
        st=f.readline()
        
          
        for s in st:
         #   print(s)
            if s=='.':
                k1.append(-1)
            elif s!='\n':
                k1.append(int(s))
                
        k.append(k1)
    
  #  print (k)
    
    wp=[]
    for i in k:
        wp1=0
        ob=0
        for j in i:
            if j!=-1:
                ob+=1
                if j==1:
                    wp1+=1
        wp.append(wp1/ob)
        
 #   print ('wp=',wp)

    owp=[]
    for i1 in range(n):
        s=0    
        kol=0
        for i in range(n):
            owp1=0
            ob=0
            if k[i1][i]!=-1:
                kol+=1
            for j in range(n):
                if k[i][j]!=-1 and i!=i1 and j!=i1:
                    ob+=1
                    
                    if k[i][j]==1:
                        owp1+=1
            if k[i1][i]!=-1 and ob!=0:
                s=s+owp1/ob
           #     print (i1,i,owp1,ob,s,kol)
        owp.append(s/kol)
  #  print ('owp=',owp)    
    
    
    oowp=[]
    for i in range(n):
        oowp1=0
        kol=0
        s=0
        for j in range(n):
            if k[i][j]!=-1:
                kol+=1
                s+=owp[j]
           #     print (i,j,owp[j],kol,s)
        
        oowp.append(s/kol)
        
  #  print ('oowp=',oowp)       
 
    rpi=[]
    for i in range(n):
        rpi.append(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i])
        
    print (rpi)
    for i in range(n):
        f1.write(str(rpi[i])+'\n')
 #   print ('Case #'+str(t)+' ',d)  
  #  if d:
  #      f1.write('Case #'+str(t)+': Possible\n')
 #   else:
   #      f1.write('Case #'+str(t)+': Broken\n')   
         
             
            


f.close()
f1.close()
     
end1 = clock()

print (' время= ',end1-start1)
