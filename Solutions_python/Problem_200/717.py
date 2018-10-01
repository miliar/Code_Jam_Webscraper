def func(N):
    arr=[int(e) for e in str(N)]
    while 1:
        arr1=arr[1:]
        for i,(d,p)in enumerate(zip(arr,arr1)):
            if p<d:break
        else:return int(''.join(str(e) for e in arr))
        arr[i]=arr[i]-1
        l=len(arr)
        for j in range(i+1,l):arr[j]=9
for i in range(1,input()+1):
    r=func(input())
    print "Case #"+str(i)+": "+str(r)