F=open("B-small-attempt1.in","r")
FO=open("ouput.txt","w")
N=F.read().splitlines()
for G in range(1,int(N[0])+1):
    temp=str(N[G])
    if len(temp)==1:
        FO.write("Case #"+str(G)+": "+temp+"\n")
    else:
        if all(int(x)<=int(y) for x,y in zip(temp,temp[1:]))==True:
            FO.write("Case #"+str(G)+": "+temp+"\n")
        else:
            while all(int(x)<=int(y) for x,y in zip(temp,temp[1:]))!=True:
                temp=int(temp)
                temp-=1
                temp=str(temp)
            FO.write("Case #"+str(G)+": "+temp+"\n")
F.close()
FO.close()
