# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(raw_input())):
    n,m,x=map(int,raw_input().split())
    a=map(int,raw_input().split())
    b=map(int,raw_input().split())
    suma=[0 for i in range(len(a))]
    sumb=[0 for j in range(len(b))]
    suma[0]=a[0]
    sumb[0]=b[0]
    mxcnta=0
    mxcntb=0
    if suma[0]<=x:
        mxcnta=1
    if sumb[0]<=x:
        mxcntb=1
    for i in range(1,max(len(a),len(b))):
        if i<len(a):
            suma[i]=suma[i-1]+a[i]
            if suma[i]<=x:
                mxcnta=i+1
        if i<len(b):
            sumb[i]=sumb[i-1]+b[i]
            if sumb[i]<=x:
                mxcntb=i+1
    mxcnt=max(mxcnta,mxcntb)
    mxcntl=mxcnt
    #for finding upperbound
    while True:
        mxcntl=mxcnt
        mxcnt=mxcnt*2
        flag=False
        if mxcnt<=len(a)+len(b):
            for j in range(0,mxcnt/2):
                if ((j<len(a) and mxcnt-j-2<len(b)) and (suma[j]+sumb[mxcnt-j-2]<=x)) or ((j<len(b) and mxcnt-j-2<len(a)) and (suma[mxcnt-j-2]+sumb[j]<=x)):
                    flag=True
                    break
           # if (mxcnt/2-1<len(a) and suma[mxcnt/2-1]<=x) or (mxcnt/2-1<len(b) and sumb[mxcnt/2-1]<=x):
            #    flag=True
            if flag==False:
                break
        else:
            mxcnt=len(a)+len(b)
            break
    #print mxcnt,mxcntl
    while mxcntl<=mxcnt and mxcnt<=len(a)+len(b):
        flag=False
        mid=(mxcntl+mxcnt)/2
        #cnt+=1
        #print mid
        if mid<=len(a)+len(b):
            for j in range(0,mid/2):
                if ((j<len(a) and mid-j-2<len(b)) and (suma[j]+sumb[mid-j-2]<=x)) or ((j<len(b) and mid-j-2<len(a)) and (suma[mid-j-2]+sumb[j]<=x)):
                    flag=True
                    mxcntl=mid+1
                    #print mxcntl,mxcnt
                    break
            if (mid-1<len(a) and suma[mid-1]<=x) or (mid-1<len(b) and sumb[mid-1]<=x):
                flag=True
                mxcntl=mid+1
                #print mxcntl,mxcnt,9
            if flag==False:
                mxcnt=mid-1
        else:
            break
    if mxcntl==0:
        print 0
    else:
        print mxcntl-1
        
            
