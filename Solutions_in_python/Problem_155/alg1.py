import sys
sys.setrecursionlimit(1500)


n = int(input())



def alg(smax,s):
    if smax == 0:
        return (int(s[0]),0)
    else:
        ntotal, najout = alg(smax-1,s[:-1])
        
        cur = int(s[-1])

        if ntotal >= smax:
            return (ntotal+cur,najout)
        else:
            ajoute = smax-ntotal
            return (ntotal+cur+ajoute,najout+ajoute) 


for i in range(n):
    data = [x for x in input().split()]
    smax, s = int(data[0]), data[1]

    print("Case #",i+1,": ",alg(smax,s)[1],sep="")




