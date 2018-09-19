import re
def mod(num):
    if num<0:
        num= -num
    return num    

def cycle(arr):
    arr1=[]
    arr1+=[arr[-1]]
    for i in range(len(arr)-1):
        arr1+=[arr[i]]
    return arr1

def triplets(num):
    trips=[]
    for i in range(10,-1,-1):
        for j in range(10,-1,-1):
            for k in range(10,-1,-1):
                if i+j+k==num and (mod(i-j)<=2 and mod(j-k)<=2 and mod(i-k)<=2):
                    if list(sorted([i,j,k])) not in trips:
                        trips+=[list(sorted([i,j,k]))]
    return trips
text=open('C:\\Users\\Anshul\\Downloads\\B-small-attempt0.in','r')
N=int(text.readline())
for j in range(N):
    line=text.readline()
    ns=re.findall('\d+',line)
    arr=[]
    n=int(ns[1])
    n2=int(ns[2])
    for i in range(int(ns[0])):
        arr+=[triplets(int(ns[3+i]))]
    maxcount=0
    for i in range(len(arr)):
        arr=cycle(arr)
        arr1=[]
        n1=0
        for element in arr:
            if len(element)>1:
                if n1==n:
                    arr1+=[element[1]]
                elif n1<n:
                    arr1+=[element[0]]
                    n1+=1
            else:
                i=element[0][0]
                l=element[0][1]
                k=element[0][2]
                if mod(i-l)==2 or mod(l-k)==2 or mod(i-k)==2:
                    n1+=1
                arr1+=[element[0]]
        count=0
        for element in arr1:
            if max(element)>=n2:
                count+=1
        if count>maxcount:
            maxcount=count
    f=open('C:\\Users\\Anshul\\Downloads\\out11.txt','a')
    f.write('Case #'+str(j+1)+': '+str(maxcount)+'\n')
f.close()
