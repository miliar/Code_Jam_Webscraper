import copy

def readfile(f): 
    data=[]
    lines = f.readlines()
    for line in lines:
        line=line.strip('\n')
        line=line.split(' ')
        line=map(float,line)
        data.append(line),                    
    f.close()
    return data

def War(a,b):
    if a[-1]>b[-1]:
        ifwin=1
        del a[-1]
        del b[0]
    else:
        ifwin=0
        del a[-1]
        del b[-1]
    return (a,b,ifwin)

def dWar(A,B):
    if A[0]>B[0]:
        ifwin=1
        del A[0]
        del B[0]
    else:
        ifwin=0
        del A[0]
        del B[-1]
    return (A,B,ifwin)

    
f=file('D-large.in','r')
data=readfile(f)
f.close()

num=int(data[0][0])
del data[0]
label1=[]
label2=[]

for n in range(0,num):
    N=int(data[n*3][0])
    A=data[n*3+1]
    B=data[n*3+2]
    A.sort()
    B.sort()
    a=copy.deepcopy(A)
    b=copy.deepcopy(B)
    count1=0
    count2=0
    while len(A)>0:
        (A,B,ifwin)=dWar(A,B)
        count1+=ifwin
    label1.append(count1)
    while len(a)>0:
        (a,b,ifwin)=War(a,b)
        count2+=ifwin
    label2.append(count2)
    
f2=file('D_large_output.in','w')
for i in range(0,num):
    f2.write("Case #%d: %d %d\n" % (i+1,label1[i],label2[i]))
f2.close()
