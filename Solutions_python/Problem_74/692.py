def solvecase(T):
    l = int(T[0])
    numbers = list(map(int,T[2::2]))
    names = T[1::2]
    ol = []
    bl = []
    op = bp = 1
    done = 0
    t = 0
    for i in range(l):
        if names[i]=='B':
            bl.append(numbers[i])
        elif names[i]=='O':
            ol.append(numbers[i])
    while(done<l):
        t+=1
        flag = False
        #Atlas
        if len(bl)>0:
            if bl[0]==bp:
                if names[0]=='B': #push
                    bl.pop(0)
                    numbers.pop(0)
                    names.pop(0)
                    done+=1
                    flag = True
            elif bl[0]>bp: bp+=1
            elif bl[0]<bp: bp-=1
        #P-Body
        if len(ol)>0:
            if ol[0]==op:
                if names[0]=='O' and not flag: #push
                    ol.pop(0)
                    numbers.pop(0)
                    names.pop(0)
                    done+=1
            elif ol[0]>op: op+=1
            elif ol[0]<op: op-=1
    return t

def parseandsolve(s):
    return solvecase(s.split(' '))
        
N = int(input())

for n in range(N):
    r = parseandsolve(input())
    print("Case #"+str(n+1)+": "+str(r))
