t=input()

for i in range(t):
    inpt=map(int,raw_input().split(" "))
    N=inpt[0]
    K=inpt[1]
    if K==N:
        print "Case #"+str(i+1)+": "+"0 0"

    else:
        Stalls=["O"]

        count1=0
        while count1<N:
            Stalls.append(".")
            count1+=1
        Stalls.append("O")

        while K>0:
            data=[]

            for x in range(len(Stalls)):
                if Stalls[x]==".":
                    count2=0
                    while Stalls[x-count2]!="O":
                        count2+=1
                    Ls=count2

                    count3=0
                    while Stalls[x+count3]!="O":
                        count3+=1
                    Rs=count3

                    data.append([x,min(Ls,Rs),max(Ls,Rs)])

            data= sorted(data, key=lambda x: (x[1], x[2],-x[0]))
            Stalls[data[-1][0]]="O"
            K-=1
        print "Case #"+str(i+1)+": "+str(data[-1][2]-1)+" "+str(data[-1][1]-1)







