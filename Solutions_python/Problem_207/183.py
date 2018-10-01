infilecode = "BLI"

import sys
#import networkx as nx
mapping = {"A":"A", "B":"B", "C":"C", "D":"D", "E":"E", "X":"example", "S":"-small", "L":"-large", "P":"-practice", "0":"-attempt0", "1":"-attempt1", "2":"-attempt2", "I":".in", "T":".txt"}
infile = "".join(mapping[c] for c in infilecode)
outfile = infile.replace(".in", "") + ".out.txt"
sys.stdin = open(infile, 'r')
output = open(outfile, 'w')

T = int(input())

for case in range(1,T+1):
    
    N, R, O, Y, G, B, V = list(map(int, input().split()))
    
    print(N, R, O, Y, G, B, V)
    start = [N, R, O, Y, G, B, V]

    B -= O
    Y -= V
    R -= G

    X = [B,Y,R]
    c = ["B","Y","R"]

    N = B+Y+R

    answer = "IMPOSSIBLE"

    if min(X) < 0:
        answer = "IMPOSSIBLE"
    elif max(X) == 0:
        if O and not V and not G:
            answer = "OB"*O
        elif V and not O and not G:
            answer = "VY"*V
        elif G and not V and not O:
            answer = "GR"*G

    elif O and not B: answer = "IMPOSSIBLE"
    elif V and not Y: answer = "IMPOSSIBLE"
    elif G and not R: answer = "IMPOSSIBLE"

    elif max(B,Y,R)*2 > N:
        answer = "IMPOSSIBLE"
    else:
        #by = (B+Y-2*R)//2
        
        if B == max(X):
            ss = "B"*B + "Y"*Y + "R"*R
        if Y == max(X):
            ss = "Y"*Y + "B"*B + "R"*R
        if R == max(X):
            ss = "R"*R + "B"*B + "Y"*Y
        #print(ss)
        answer = [""]*N
        for i in range(N):
            new = i*2
            if i*2 >= N:
                if N%2 == 1:
                    new -= (N)
                else:
                    new -= (N-1)
            #print(new)
            answer[new] = ss[i]
        #answer = ""
        #y = sorted( (X[i],c[i]) for i in range(3))
        #answer +
        answer = "".join(answer)
        if G:
            a = answer.index("R")
            answer = answer[:a] + "RG"*G + answer[a:]
        if O:
            a = answer.index("B")
            answer = answer[:a] + "BO"*O + answer[a:]
        if V:
            a = answer.index("Y")
            answer = answer[:a] + "YV"*V + answer[a:]


    

    #answer = N, R, O, Y, G, B, V
    if 0 and answer != "IMPOSSIBLE":
        if answer.count("B") != B:
            exit()
        if answer.count("R") != R:
                exit()
        if answer.count("Y") != Y:
                exit()
        if answer[0] == answer[-1]:
            exit()
        if answer.count("BB"):
                exit()
        if answer.count("OO"):
                exit()
        if answer.count("YY"):
                exit()


    print("Case #%d:" % case, answer)
    print("Case #%d:" % case, answer, file = output)