import sys


fin = sys.stdin
fout = sys.stdout
ferr = sys.stderr

T = int(fin.readline())

for case in range(T):
    l = fin.readline()
    D = int(l.split()[0])
    N = int(l.split()[1])
    maxt = -float("inf")
    for i in range(N):
        l = fin.readline()
        K = int(l.split()[0])
        S = int(l.split()[1])        
        t = (D-K)/S
        maxt = max(maxt,t)
    v = D / maxt

    fout.write("Case #%i: %.7f\n" % (case+1, v))

