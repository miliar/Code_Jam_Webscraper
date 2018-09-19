import sys

g=[]
r=[]
m=None

def calc(r,s):
    s1=[x for x in s]
    t=len(r)
    c=0
    for i in r:
        for j in range(len(s)/t):
            s1[c+(j*t)]=s[i+(j*t)]
        c+=1

    o=None
    c=0
    for i in s1:
        if o!=i:
            c+=1
            o=i
    return c

def gen(k,s):
    global g,r,m

    if k<=0: 
        res=calc(r,s)
        if m==None: m=res
        elif m>res: m=res

    for i in range(len(g)):
        if g[i]==0:
            g[i]=1
            r.append(i)
            gen(k-1,s)
            r.pop()
            g[i]=0
    
    

def RLE(k,s):
    global g,m
    m=None
    g=[0 for x in range(k)]
    gen(k,s)

    return m

def go(name):
    f=file(name)

    line=f.readline().strip()
    total=int(line)
    for i in range(total):
        k=int(f.readline().strip())
        s=f.readline().strip()

        print "Case #%d: %d" %(i+1, RLE(k,s))
    f.close()

try:
    fn=sys.argv[1]
except:
    print "Usage:\n", "python", sys.argv[0]+" input_file_name"
    sys.exit(1)

go(fn)
