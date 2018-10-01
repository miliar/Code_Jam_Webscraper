def slow(x,v):
    for i in range(len(x)):
        for j in range(i):
            if(x[i]==x[j]):
                if(v[i]<v[j]):
                    v[j]=v[i]
                else:
                    v[i] = v[j]    
    return x,v

input = open("input.txt","r")    
output = open("output.txt","w+")
cases = int(input.readline())

for case in range(1,cases+1):
    print("--")
    output.write("Case #%d: "%case)
    v = []
    x = []
    n,k,b,t = map(int,input.readline().rstrip().split())
    x = input.readline().rstrip().split()
    v = input.readline().rstrip().split()
    x.reverse()
    v.reverse()
    x,v = slow(x,v)
    out =[]
    suc = 0
    fai = 0
    swaps = 0
    print(n)
    print(k)
    for i in range(n):
        if(int(v[i])>0):
            pos = (b-int(x[i]))/int(v[i])
            if(pos<=t):
                out.append("1")
                suc+=1
            else:
                out.append("0")
                fai+=1
        else:
            out.append("0")
        if(suc>=k):
            print("POSSIBLE")
            stpl = -1
            fac = 0
            try:
                stpl = out.index("0",0)
            except ValueError:
                pass
            print(stpl)
            if(stpl>-1):
                for j in range(stpl,len(out)):
                    if(out[j]=="0"):
                        fac+=1
                    else:
                        swaps+=fac
            output.write("%d\n"%swaps)        
            break
        if(fai>(n-k)):
            output.write("IMPOSSIBLE\n")
            print("IMPOSSIBLE")
            break
    print(out)
    print(swaps)