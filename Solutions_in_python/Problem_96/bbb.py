f=open("large.txt","r")
lists=f.readlines()
tests=int(lists[0])
i=1
while i<=tests:
    values=lists[i].split(' ')        
    int_val=[int(each) for each in values]
    n=int_val[0]
    sur=int_val[1]
    max_val=int_val[2]
    k=3
    final=0
    if max_val!=0:
        while n>0:
            if int_val[k]==0:
                k=k+1
                n=n-1
                continue
            x=int_val[k]%3
            div_val=int_val[k]/3
            if x==1:            
                if max_val<=div_val+1:
                    final+=1
            elif x==0:            
                if max_val<=div_val:
                    final+=1
                elif max_val<=div_val+1:
                    if sur>0 and (int_val[k]>=2 and int_val[k]<=28):
                        sur-=1
                        final+=1
            elif x==2:
                if max_val<=div_val+1:
                    final+=1
                elif max_val<=div_val+2:
                    if sur>0 and (int_val[k]>=2 and int_val[k]<=28):
                        sur-=1
                        final+=1
            k=k+1
            n=n-1
    else:
        final=n
    print "Case #%d: %d" %(i,final)
    i=i+1
