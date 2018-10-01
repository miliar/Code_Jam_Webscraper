f=open("inp.txt","r")
lists=f.readlines()
tests=int(lists[0])
i=1
while i<=tests:
    values=lists[i].split(' ')        
    i_val=[int(each) for each in values]
    num=i_val[0]
    sup=i_val[1]
    m_val=i_val[2]
    t=0
    k=3
    if m_val!=0:
        while num>0:
            if i_val[k]==0:
                k=k+1
                num=num-1
                continue
            x=i_val[k]%3
            d_val=i_val[k]/3
            if x==1:            
                if m_val<=d_val+1:
                    t+=1
            elif x==0:            
                if m_val<=d_val:
                    t+=1
                elif m_val<=d_val+1:
                    if sup>0 and (i_val[k]>=2 and i_val[k]<=28):
                        sup-=1
                        t+=1
            elif x==2:
                if m_val<=d_val+1:
                    t+=1
                elif m_val<=d_val+2:
                    if sup>0 and (i_val[k]>=2 and i_val[k]<=28):
                        sup-=1
                        t+=1
            k=k+1
            num=num-1
    else:
        t=num
    print "Case #%d: %d" %(i,t)
    i=i+1
