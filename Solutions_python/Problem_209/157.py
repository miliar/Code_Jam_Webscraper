#!/usr/bin/python3

pp=0
#pp=1

from math import pi

if (pp):
    def pprint(*ll):
        print("".join(map(str,list(ll))))
else:
    def pprint(*ll):
        1


def M():
    t = int(input())
    for i in range(1, t + 1):
        print("Case #%d: "%i,end="")
        solve()


def solve():
    #pprint("solve {}".format(s))
    n,k=map(int,input().split())
    rad=[]
    ht=[]
    for i in range(n):
        r,h = map(int,input().split())
        rad.append(r)
        ht.append(h)
    asort = sorted(range(n), key=lambda x: -rad[x]*ht[x])
    rsort = sorted(range(n), key=lambda x: -rad[x])
    pprint("sorted order: ",asort)
    pprint("r sorted order: ",rsort)
    best = -1.0
    pprint("n=%d,k=%d"%(n,k))
    for tt in range(n-k+1):
        t = rsort[tt] # outer radius index
        rt = rad[t]
        tbest = rt*(rt+2*ht[t]) # pi r^2 + 2 pi r h
        i = 0 # asort index
        j = 1 # added up to k (will succeed)
        while j<k:
            #pprint("i=%d, j=%d"%(i,j))
            ai = asort[i]
            rai = rad[ai]
            if (ai!= t and rai<=rt):
                j+=1
                tbest += rai *2*ht[ai]
            else:
                pprint("t=%d, ai=%d, rt= %f, rai=%f"%(t,ai,rt,rai))
            i+=1
        if tbest>best:
            best =tbest
    print(best * pi)

    
    
def cl(line):
    return sum([1 if x!="?" else 0 for x in line])

def sline(line):
    for c in line:
        if c != "?":
            break
    for i in range(len(line)):
        if line[i]=="?":
            line[i]=c
        elif line[i]!="c":
            c=line[i]


def scake(cake):
    l=0
    while(cl(cake[l])==0):
        l+=1

    pprint("first nonempty %d"%l)
    sline(cake[l])
    for i in range(l):
        cake[i]=cake[l]
        pprint("%d from %d"%(i,l))

    while True:
        m = l+1
        while(m<len(cake) and cl(cake[m])==0):
            m+=1
        if m==len(cake):
            for i in range(l+1,m):
                pprint("%d,%d,%s,%s"%(i,l,cake[i],cake[l]))
                cake[i] = cake[l]
                pprint("%d,%d,%s,%s"%(i,l,cake[i],cake[l]))
                pprint(". %d from %d"%(i,l))
            break
        sline(cake[m])
        for i in range(l+1,m):
            cake[i]=cake[l]
            pprint(".. %d from %d"%(i,l))
        l=m

    for i in range(len(cake)):
        print("".join(cake[i]))
    


M()
    
