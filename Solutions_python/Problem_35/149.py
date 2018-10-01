arr=[]
mid=[]
ret=[]
h=0
w=0
def getmin(h,w,i,j,n):
    min=[]
    minn=n
    if i!=0 and minn>arr[i-1][j]:
        min=[i-1,j]
        minn=arr[i-1][j]
    if j!=0 and minn>arr[i][j-1]:
        min=[i,j-1]
        minn=arr[i][j-1]
    if j!=w-1 and minn>arr[i][j+1]:
        min=[i,j+1]
        minn=arr[i][j+1]
    if i!=h-1 and minn>arr[i+1][j]:
        min=[i+1,j]
        minn=arr[i+1][j]
    return min
def getneighbors(h,w,ii,jj):
    rett=[]
    if ii!=0:
        rett.append([ii-1,jj])
    if jj!=0:
        rett.append([ii,jj-1])
    if jj!=w-1:
        rett.append([ii,jj+1])
    if ii!=h-1:
        rett.append([ii+1,jj])
    return rett

ptr=96
def flood(i,j,h,w):
    if ret[i][j]!='':
        return
    ret[i][j]=chr(ptr)
    l=getneighbors(h,w,i,j)
    if mid[i][j]!=[]:
        flood(mid[i][j][0],mid[i][j][1],h,w)
    for k in l:
        if ret[k[0]][k[1]]=='' and mid[k[0]][k[1]]==[i,j]:
            flood(k[0],k[1],h,w)
    
n=input()
for qq in range(n):
    tt=raw_input()
    tt=[int(x) for x in tt.split(' ')]
    h=tt[0]
    w=tt[1]
    arr=[]
    mid=[]
    ret=[]
    ptr=96
    for a in range(h):
        arr.append([])
        mid.append([])
        ret.append([])
        for b in range(w):
            arr[a].append(0)
            mid[a].append('')
            ret[a].append('')

    for a in range(h):
        tt=raw_input()
        arr[a]=[int(x) for x in tt.split(' ')]

    for i in range(h):
        for j in range(w):
            mid[i][j]=getmin(h,w,i,j,arr[i][j])
    
    for i in range(h):
        for j in range(w):
            if ret[i][j]=='':
                ptr+=1
                flood(i,j,h,w)
    print 'Case #'+str(qq+1)+':'
    for i in range(h):
        print ' '.join(ret[i])