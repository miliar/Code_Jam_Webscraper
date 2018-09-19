def solve(c,f,x):
    
    
    time=x/2
    time2=x/2
    time3=0
    v1=2
    v2=0
    
    while(1):
       v2=v1+f
       time3+=round(c/v1,7)
       time2=round(x/v2,7)+round(time3,7)
      
    
      
       v1=v2
       if(time2>time):
                           return time
       
       time=time2
    



L=list()
f2 = open('B-small-attempt0.in','r')
f3 = file('g_2.in','w')
for i in f2:
    tmp=''
    tmp="".join(i)
    r=tmp.split('\n')
    r=r[0].split(' ')
    L.append(r)    
        
  
n=int(L[0][0])
print(n)
i=1
j=11
print(L[1][0])
for k in range(1,n+1):
               
                case=solve(float(L[k][0]),float(L[k][1]),float(L[k][2]))
                tmp=''
               
                tmp="Case #"+str(k)+": "+str(case)+'\n'
                    
                
                print(tmp)
                f3.write(tmp)







f2.close

f3.close



