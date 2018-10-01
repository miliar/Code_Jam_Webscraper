# -*- coding: utf-8 -*-

fin = open("c.in","r")
T = int(fin.readline())

S = "welcome to code jam"
N = len(S)

for t in range(T):
    string = fin.readline().strip()
    
    M = len(string)
    Nk = [1]*(M+1)
    
    for c in S:
        k = Nk
        Nk = [0]*(M+1)
        
        for i, d in zip(range(1, M+1), string):
            Nk[i] = Nk[i-1]
            if c == d:
                Nk[i] += k[i-1]
                while Nk[i] > 10000:
                    Nk[i] -= 10000
        
    s = str(Nk[-1])
    while len(s) < 4:
        s = "0" + s
    print "Case #%d: %s" % (t+1, s)