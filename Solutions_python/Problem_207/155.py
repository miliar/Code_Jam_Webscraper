def solveRBY(R, B, Y):
    occ = {"R":R, "B":B, "Y":Y}
    colorrank = sorted("RBY", key=lambda c: -occ[c])
    Q, W, E = sorted([R, B, Y], reverse=True)
    if Q > W+E:
        return "IMPOSSIBLE"
    config = "QWE"*(W+E-Q) + "QW"*(Q-E) + "QE"*(Q-W)
    return config.replace("Q",colorrank[0]).replace("W",colorrank[1]).replace("E",colorrank[2])

def solve(R, O, Y, G, B, V):
    if O==Y==B==V==0:
        return "RG"*R if R==G else "IMPOSSIBLE"
    if R==Y==G==V==0:
        return "OB"*B if O==B else "IMPOSSIBLE"
    if R==O==G==B==0:
        return "YV"*Y if Y==V else "IMPOSSIBLE"
    R-= G
    B-= O
    Y-= V
    if R<0 or B<0 or Y<0:
        return "IMPOSSIBLE"
    if (R==0 and G>0) or (B==0 and O>0) or (Y==0 and V>0):
        return "IMPOSSIBLE"
    s = solveRBY(R, B, Y)
    if s == "IMPOSSIBLE":
        return "IMPOSSIBLE"
    convert = []
    for c in s:
        if c == "R" and G > 0:
            convert.append("R"+"GR"*G)
            G = 0
        elif c == "B" and O > 0:
            convert.append("B"+"OB"*O)
            O = 0
        elif c == "Y" and V > 0:
            convert.append("Y"+"VY"*V)
            V = 0
        else:
            convert.append(c)
    return ''.join(convert)

'''
def validate(R, O, Y, G, B, V, s):
    if s == "IMPOSSIBLE":
        print(R, O, Y, G, B, V, s)
        return
    num = [R,O,Y,G,B,V]
    col = "ROYGBV"
    for i in range(6):
        if s.count(col[i]) != num[i]:
            print(R, O, Y, G, B, V, s)
            raise Exception
    for i in range(len(s)):
        if s[i]+s[(i+1)%len(s)] in "RR YY BB RV RO YO YG BG BV OO GG VV OR OY OG OV GO GY GB GV VR VO VG VB":
            print(R, O, Y, G, B, V, s)
            raise Exception
    print(R, O, Y, G, B, V, s)

import random
def rangen():
    s = random.choice(["R", "Y", "B", "O", "G", "V"])
    while 1:
        c = random.choice(["R", "Y", "B", "O", "G", "V"])
        if s[-1]+c in "RR YY BB RV RO YO YG BG BV OO GG VV OR OY OG OV GO GY GB GV VR VO VG VB":
            continue
        s+= c
        if random.random()<0.01 and c+s[0] not in "RR YY BB RV RO YO YG BG BV OO GG VV OR OY OG OV GO GY GB GV VR VO VG VB":
            break
    return s.count("R"), s.count("O"), s.count("Y"), s.count("G"), s.count("B"), s.count("V"), s

for i in range(100):
    R, O, Y, G, B, V, s = rangen()
    validate(R, O, Y, G, B, V, s)
    if solve(R, O, Y, G, B, V) == "IMPOSSIBLE":
        raise Exception
    validate(R, O, Y, G, B, V, solve(R,O,Y,G,B,V))
'''

for T in range(int(input())):
    a, R, O, Y, G, B, V = map(int,input().split())
    solved = solve(R, O, Y, G, B, V)
    print("Case #%d: %s"%(T+1,solved))
