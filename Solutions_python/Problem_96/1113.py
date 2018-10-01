import string
f=open('B-large.in','r')
o=open('output.txt','w')

case=0
for line in f:
    if case==0:
        maxlines=line
        case+=1
        continue
    s=line.split()
    num_gog=s[0]
    surp=s[1]
    best=s[2]
    count=0
    check=0
    
    for i in range(3,len(s)):
        temp=int(s[i])-int(best)
        if temp<0:
            continue
        if temp>=2*int(best)-2:
            count+=1
        elif temp>=2*int(best)-4:
            check+=1
        
    count=count+min(check,int(surp))
   
    o.write('Case #'+str(case)+': '+str(count)+'\n')
    case+=1    





f.close()
o.close()


