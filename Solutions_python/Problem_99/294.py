fin = open("A-small.in",'r')
fout = open("output.out",'w')

tmp = fin.readline()
T = eval(tmp)
for t in range(T):
    tmp = fin.readline().split()    
    a = eval(tmp[0])
    b = eval(tmp[1])
    p = []
    tmp = fin.readline().split()
    for i in range(a):
        p.append(eval(tmp[i]))
    k = []
    tp = 1
    P = []
    for i in range(a):
        tp = tp * p[i]
        P.append(tp)
    P.reverse()
    for i in range(a):
        k.append(P[i] * (b - a + 1 + 2 * i) + (1 - P[i]) * (2 * b - a + 2 + 2 * i))
    k.append(2 + b)
    print >> fout, "Case #%d: %.6lf" % ((t + 1),min(k))
fin.close()
fout.close()