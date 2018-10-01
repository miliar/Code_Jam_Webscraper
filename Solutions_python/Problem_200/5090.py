def tidy():
    T=int(input())
    for i in range(T):
        N=int(input())
        flag=1
        j=N
        count=0
        rep=0
        while(flag==1 and j>=1):
            count=0
            arr=[]
            rep=j
            while(rep>0):
                arr.append(rep%10)
                rep=rep//10
            for k in range(len(arr)-1):
                if arr[k]>=arr[k+1]:
                    count=count+1
            if (count==len(arr)-1):
                flag=0
                break
            j=j-1
        print("Case #%d:%d",%(i+1,j))

tidy()
