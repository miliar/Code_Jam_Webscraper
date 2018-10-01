
pi=open("D:\\output.txt","w")

n=int(raw_input())

for l in range(n):

    count=0
    num=0

    inp=raw_input().split()

    ger=inp[1]

    for i in range(len(ger)):
        
        if(i>count and ger[i]!='0'):
            num+=(i-count)
            count+=num
        count+=int(ger[i])

    print num

    pi.write("Case #"+str(l+1)+": "+str(num)+"\n")


pi.close()

        
