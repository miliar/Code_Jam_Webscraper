f=open('A-small-attempt7.in','r')
f2=open('output.txt','w')
test=int(f.readline())
#print test
for x in range(0,test):
    n=f.readline()
    c=len(n)
    pos_o=1
    pos_b=1
    time1=0
    prev=2
    reduction=0
    for y in range(2,c):
        temp=''
        i=2
        if n[y]=='B':
            while (n[y+i]!=' ' and n[y+i]!='\n'):
                temp+=n[y+i]
                i+=1
            temp=int(temp)
            if prev==1 or prev==2:
                time1+=abs(temp-pos_b)+1
                reduction+=abs(temp-pos_b)+1
            else:
                temp2=abs(temp-pos_b)-reduction
                if temp2<0:
                    temp2=0
                time1+=temp2+1
                reduction=temp2+1
            pos_b=temp
            prev=1
        elif n[y]=='O':
            while (n[y+i]!=' ' and n[y+i]!='\n'):
                temp+=n[y+i]
                i+=1
            temp=int(temp)
            if prev==0 or prev==2:
                time1+=abs(temp-pos_o)+1
                reduction+=abs(temp-pos_o)+1
            else:
                temp2=abs(temp-pos_o)-reduction
                if temp2<0:
                    temp2=0
                time1+=temp2+1
                reduction=temp2+1
            pos_o=temp
            prev=0
        elif n[y]=='\n':
            break
        else:
            continue
    print 'Case #'+str(x+1)+': '+str(time1)
    f2.write('Case #'+str(x+1)+': '+str(time1)+'\n')
f2.close()
f.close()
