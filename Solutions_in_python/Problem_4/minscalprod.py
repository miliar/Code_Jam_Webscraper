strptime = lambda str : datetime.strptime(str, "%H:%M")
readfromline = lambda func : [func(input) for input in str(raw_input()).split()]
scalprod = lambda v1, v2: (v1[x]+v2[x] for x in range(len(v1)))

if __name__ == '__main__':
    t=int(raw_input())
    for x in range(t):
        n=int(raw_input())
        v1=readfromline(int)
        v2=readfromline(int)
        v1.sort()
        v2.sort()
        tot=0
        for i in range(len(v1)):
            tot+=v1[i]*v2[-i-1]
        print 'Case #'+str(x+1)+': '+str(tot)