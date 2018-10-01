T = int(input())
for z in range(T):
    N = int(input())
    Nlist = [int(x) for x in str(N)]
    prev = 0;
    for i in range(len(Nlist)):
        if(Nlist[prev]<Nlist[i]):
            prev = i
        elif(Nlist[prev]>Nlist[i]):
            Nlist[prev] = Nlist[prev]-1
            for i in range(prev+1,len(Nlist)):
                 Nlist[i] = 9
            break;
    if 0 in Nlist: Nlist.remove(0)
    final =''.join(str(x) for x in Nlist)
    if(final[0] == "0"):
        final[0] = ""
    if(z == T-1):
        print("Case #"+str(z+1)+": "+ final,end="")
    else:
        print("Case #"+str(z+1)+": "+ final)
