#!/usr/bin/python
def pick_best(first, lc, R, Y, B):
    #print R, Y, B, lc
    if R >= Y and R >= B and lc != "R":
        return "R"
    if R >= Y and R >= B and lc == "R":
        if Y == B:
            if first == "B":
                return "B"
            else:
                return "Y"
        if Y > B:
            return "Y"
        else:
            return "B"

    if Y > R and Y >= B and lc != "Y":
        return  "Y"

    if Y > R and Y >= B and lc == "Y":
        if B == R:
            if first == "B":
                return "B"
            else:
                return "R"
        if R >= B:
            return "R"
        else:
            return "B"
    if B > R and B > Y and lc != "B":
        return "B"
    if B > R and B > Y and lc == "B":
        if R >= Y:
            return "R"
        else:
            return "Y"
    return "O"

def ans(s, R, Y, B):
    lc = s
    while R + Y + B > 0:
        n = pick_best(s[0], lc, R, Y, B)
        if n == "R":
            R = R-1
        elif n == "Y":
            Y = Y-1
        else:
            B = B-1
        s = s+n
        lc = n
    table = {"R" : 0, "Y" : 0, "B" : 0}
    lis = []
    for i in s:
        lis.append(i)
    if lis[0] == lis[len(s) - 1]:
        lis[len(s) - 2], lis[len(s) - 1] = lis[len(s) - 1], lis[len(s) - 2]
    s = ''.join(lis)
    for i in s:
        table[i] += 1
    #print "TES", table["R"] + table["Y"] + table["B"], table["R"], 0, table["Y"],0, table["B"], 0
    return s

T = int(raw_input())
for i in range(T):
    l = raw_input().split()
    R = int(l[1])
    Y = int(l[3])
    B = int(l[5])
    if (R >= Y and R >= B):
        if R > Y + B:
            #print "TES", l
            print "Case #"+str(i+1)+": "+"IMPOSSIBLE"
            continue
        else:
            s = "R"
            R = R-1
            print "Case #"+str(i+1)+": "+ans(s, R, Y, B)
    elif (Y > R and Y >= B):
        if (Y > R + B):
            #print "TES", l
            print "Case #"+str(i+1)+": "+"IMPOSSIBLE"
            continue
        else:
            s = "Y"
            Y = Y-1
            print "Case #"+str(i+1)+": "+ans(s, R, Y, B)
    else:
        if B > R + Y:
            #print "TES", l
            print "Case #"+str(i+1)+": "+"IMPOSSIBLE"
            continue
        else:
            s = "B"
            B = B-1
            print "Case #"+str(i+1)+": "+ans(s, R, Y, B)

