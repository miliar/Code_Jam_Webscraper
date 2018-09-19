import sys

def run():
    (n, A, B, C, D, x, y,M)= lines.pop().split(" ")
    n = int(n)
    A = int(A)
    B = int(B)
    C = int(C)
    D = int(D)
    x = int(x)
    y = int(y)
    M = int(M)
    l = []    
    X = x
    Y = y
    l.append([X, Y])
    for i in xrange(n-1):
        X = (A * X + B)%M
        Y = (C * Y + D)%M
        l.append([X, Y])

    count = 0
    for i in xrange(len(l)):
        for j in xrange(i+1,len(l)):
            for k in xrange(j+1,len(l)):
                xval = (l[i][0]+l[j][0]+l[k][0])/3.0
                if (xval%1 == 0):
                    yval = (l[i][1]+l[j][1]+l[k][1])/3.0
                    if (yval%1 == 0):
                        count += 1

    return count

f = open(sys.argv[1])
lines = f.readlines()
f.close()
f = open(sys.argv[1]+".result.txt","w")
lines.reverse()
times = int(lines.pop())
for k in xrange(times):
    f.write("Case #"+str(k+1)+": "+str(run())+"\n")
f.close()


    



















