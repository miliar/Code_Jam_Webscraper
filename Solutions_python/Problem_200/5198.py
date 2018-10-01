t=input()
for i in range(0,t,1):
        n=input()
        for j in range(n,0,-1):
		m=j 
                prev=m%10
                flag=0
                m/=10
                while(m):
                        rem=m%10
                        if(prev<rem):
                                flag=1
                                break
                        prev=rem
                        m/=10  
                if(flag==0): 
                        print'Case #%d: %d'%((i+1),j)
                        break

