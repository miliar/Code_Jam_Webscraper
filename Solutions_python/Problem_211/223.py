
f= open('C-small.in')
T = int(f.readline())
for i in range(T):
    l = f.readline()
    N = int(l.split()[0])
    K = int(l.split()[1])
    U = float(f.readline())
    l = f.readline().split()
    P = [float(s) for s in l]
    P = sorted(P)
    for j in range(1,N):
        if U > (P[j]-P[j-1]) * j:
            U -= (P[j]-P[j-1]) * j
            for k in range(j):
                P[k] += (P[j]-P[j-1])      
        else:
            for k in range(j):
                P[k] += 1.0 * U / j
            U = 0
        #print P,U
    for k in range(N):
        P[k] += 1.0 * U / N
    #print P
    totalP = 1
    for j in range(N):
        totalP *= P[j]
    #totalP = (totalP / N) ** N
    #if totalP > 1:
        #totalP = 1
    print 'Case #%d: %f' % (i+1,totalP)