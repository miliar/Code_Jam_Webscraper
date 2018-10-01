infile = open('B-small-attempt0.in','r')
outfile = open('output.txt', 'w')



T = int(infile.readline().strip())
out = ""
for tc in range(T):
    #print("TEST ",tc)
    out += "Case #"+str(tc+1)+": "
    
    N,V,X = infile.readline().split()
    n,v,x = (int(N),float(V),float(X))
    #print(n,v,x)
    Rh = 0
    Ch = 0
    Rl = 0
    Cl = 0
    Re = 0
    for i in range(n):
        R,C = infile.readline().split()
        r,c = (float(R),float(C))
        if C == X:
            Re += r
        elif c < x: #low tap
            Cl = (Cl*Rl + c*r)/(Rl+r)
            Rl += r
        else: #high tap
            Ch = (Ch*Rh + c*r)/(Rh+r)
            Rh += r
    #print(tc, Rh, Ch, Rl, Cl, Re)
    if Re != 0:
        mine = v / Re
    else:
        mine = -1
        
    minc = -1
    if Rl > 0 and Rh > 0:
        Vh = (v*x-v*Cl) / (Ch - Cl)
        minc = max(Vh/Rh,(v-Vh)/Rl)
    
    if mine == -1 and minc == -1:
        out += "IMPOSSIBLE"
    elif mine == -1:
        out += str(minc)
    elif minc == -1:
        out += str(mine)
    else:
        out += min(minc,mine)
        
    out += "\n"
    
print(out)
outfile.write(out)
    
outfile.close()
infile.close()