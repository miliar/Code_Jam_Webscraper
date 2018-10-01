f = open("gjc31in.txt","r")

val=["-","X","O"]

def getCol(r1,r2,r3,r4,i):
    return r1[i]+r2[i]+r3[i]+r4[i]

  
def win(a):
    X=0
    O=0
    T=0
    P=0
    for c in a:
        if c=="O":
            O+=1
        elif c=="X":
            X+=1
        elif c=="T":
            T+=1
        elif c==".":
            P+=1
    if ((X==4)or(X+T==4)): return 1 #X
    if ((O==4)or(O+T==4)): return 2 #O
    if (P==0): return 0
    return -1


T = int(f.readline())
for case in range(1,T+1):
    
    print "Case #" + str(case)+":",
    
    r1=f.readline().strip()
    r2=f.readline().strip()
    r3=f.readline().strip()
    r4=f.readline().strip()
    
    c1=getCol(r1,r2,r3,r4,0)
    c2=getCol(r1,r2,r3,r4,1)
    c3=getCol(r1,r2,r3,r4,2)
    c4=getCol(r1,r2,r3,r4,3)      
    
    d1=r1[0]+r2[1]+r3[2]+r4[3]
    d2=r1[3]+r2[2]+r3[1]+r4[0]

    R1=win(r1)
    if R1>0: print val[R1]+" won"; f.readline(); continue

    R2=win(r2)
    if R2>0: print val[R2]+" won"; f.readline(); continue

    R3=win(r3)
    if R3>0: print val[R3]+" won"; f.readline(); continue

    R4=win(r4)
    if R4>0: print val[R4]+" won"; f.readline(); continue
    


    C1=win(c1)
    if C1>0: print val[C1]+" won"; f.readline(); continue

    C2=win(c2)
    if C2>0: print val[C2]+" won"; f.readline(); continue

    C3=win(c3)
    if C3>0: print val[C3]+" won"; f.readline(); continue

    C4=win(c4)
    if C4>0: print val[C4]+" won"; f.readline(); continue
    


    D1=win(d1)
    if D1>0: print val[D1]+" won"; f.readline(); continue

    D2=win(d2)
    if D2>0: print val[D2]+" won"; f.readline(); continue

    if R1+R2+R3+R4+C1+C2+C3+C4+D1+D2!=0:
        print "Game has not completed"; f.readline(); continue
    else:
        print "Draw"; f.readline(); continue
    f.readline()
    
