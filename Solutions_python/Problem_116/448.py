l=[[(0,0),(0,1),(0,2),(0,3)],[(1,0),(1,1),(1,2),(1,3)],[(2,0),(2,1),(2,2),(2,3)],[(3,0),(3,1),(3,2),(3,3)],[(0,0),(1,0),(2,0),(3,0)],[(0,1),(1,1),(2,1),(3,1)],[(0,2),(1,2),(2,2),(3,2)],[(0,3),(1,3),(2,3),(3,3)],[(0,0),(1,1),(2,2),(3,3)],[(0,3),(1,2),(2,1),(3,0)]]

f=lambda l:(l.count("O")==3 and l.count("T")==1) or l.count("O")==4
g=lambda l:(l.count("X")==3 and l.count("T")==1) or l.count("X")==4
n=int(raw_input())
for i in range(n):
    t=[]
    for j in range(4):
        t.append(raw_input())
    m=lambda l:[t[i][j] for (i,j) in l]
    F=[f(m(j)) for j in l]
    G=[g(m(j)) for j in l]
    print "Case #"+str(i+1)+":",
    if any(F):
        print "O won"
    elif any(G):
        print "X won"
    elif sum(t[i][j]!="." for i in range(4) for j in range(4))==16:
        print "Draw"
    else:
        print "Game has not completed"
    

    if i!=n-1:
        a=raw_input()
