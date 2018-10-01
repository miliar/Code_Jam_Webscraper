import itertools
def test():
    prot=''.join(ch for ch, _ in itertools.groupby(string1[0]))
    list=[]
    for y in range(len(prot)):
        list.append([])
    for y in range(N):
        prot2=''.join(ch for ch, _ in itertools.groupby(string1[y]))
        if(prot2!=prot):
            return -1
        i=0;
        counter=0
        for j in range(len(string1[y])):
            if(prot[i]==string1[y][j]):
                counter+=1
            else:
                list[i].append(counter)
                counter=1
                i=i+1
        list[i].append(counter)

    totalChange=0
    for y in range(len(list)):
        change=0;
        list[y].sort()
        #print(len(list[y]))
        #print(len(list[y])//2)
        median=list[y][ len(list[y])//2 ]
        for i in range(len(list[y])):
            change+=abs(median-list[y][i])
        totalChange+=change
    return totalChange

fo = open("A-large.in")
fo2 = open("output.txt", mode='w')
tests = eval(fo.readline())

output=[];
for x in range(1,tests+1):
    N=eval(fo.readline())
    string1 =[];
    for y in range(1,N+1):
        string1.append((fo.readline()).strip("\n"))
    bool=test()

    if(bool==-1):
        output.append("Case #"+str(x)+": Fegla Won\n")
    else:
        output.append("Case #"+str(x)+": "+str(bool)+"\n")
fo2.writelines(output)




