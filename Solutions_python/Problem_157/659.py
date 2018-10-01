has = {}
has[(1,1)]=1
has[(1,2)]=2
has[(1,3)]=3
has[(1,4)]=4

has[(2,1)]=2
has[(2,2)]=-1
has[(2,3)]=4
has[(2,4)]=-3

has[(3,1)]=3
has[(3,2)]=-4
has[(3,3)]=-1
has[(3,4)]=2

has[(4,1)]= 4
has[(4,2)]=3
has[(4,3)]=-2
has[(4,4)]=-1
itr = has.keys()
for i in itr:
    x = i[0]
    y = i[1]
    has[(-1*x,y)]=-1*has[(x,y)]
    has[(x,-1*y)]=-1*has[(x,y)]
    has[(-1*x,-1*y)]=has[(x,y)]
def prog(l,s):
    arr = []
    for i in s:
        if(i=='1'):
            arr+=[1]
        elif(i=='i'):
            arr+=[2]
        elif(i=='j'):
            arr+=[3]
        else:
            arr+=[4]
    rarr = arr[:]
    for i in range(1,l):
        arr[i]=has[(arr[i-1],arr[i])]
    for i in range(l-2,-1,-1):
        rarr[i]=has[(rarr[i],rarr[i+1])]
    if(arr[-1]!=-1):
        return 0
    if 2 not in arr:
        return 0
    x = arr.index(2)
    if 4 not in rarr:
        return 0
    y = l-rarr[-1::-1].index(4)-1
    if(y>x):
        return 1
    else:
        return 0
        
t = input()
for i in xrange(1,t+1):
    inp = raw_input().split()
    l = int(inp[0])
    x = int(inp[1])
    s = raw_input()
    l*=x
    s=s*x
    print "Case #"+str(i)+":",
    if(prog(l,s)==1):
        print "YES"
    else:
        print "NO"
