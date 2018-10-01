def do():
    times = input()
    for i in xrange(times):
        print 'Case #%d:'%(i+1),
        calculate()

def calculate():
    N,X = map(int,raw_input().split())
    L = map(int,raw_input().split())
    L.sort()
    
    d = {}

    for di in xrange(N):
        for st in xrange(N-di):
            i,j = st,st+di
            
            if j-i == 0:
                d[i,j] = 1
            elif j-i == 1:
                if L[i]+L[j] <= X:
                    d[i,j] = 1
                else:
                    d[i,j] = 2
            else:
                if L[i]+L[j] <= X:
                    d[i,j] = d[i+1,j-1]+1
                else:
                    d[i,j] = min(d[i+1,j],d[i,j-1])+1

    print d[0,N-1]



if __name__ == '__main__':
    do()

