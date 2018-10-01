# -*- coding: utf-8 -*-

def flip(cakeS, pos, K):
    for idx in range(pos, pos+K):
        if cakeS[idx] == '-':
            cakeS[idx] = '+'
        else:
            cakeS[idx] = '-'
    
with open("A-large.in", "r") as f:
    filein = f.readlines()
        
t = int(filein[0])  # read a line with a single integer
for cnt in range(1, t + 1):
    ans = 0

    N = filein[cnt]
    S, K = [str(s) for s in filein[cnt].split(" ")]
    #print (S, K)
    intK = int(K)
    newS = []
    for sbl in S:
        if sbl == '-':
            newS.append('-')
        else:
            newS.append('+')
    #print (newS, K)    

    for idx in range(len(newS)-intK+1):
        if newS[idx] == '-':
            ans+=1
            flip(newS, idx, intK)
            #print (newS, intK)
    
    imp = 0
    for lastK in newS[-intK:]:
        if lastK == '-':
            imp = 1
            break
    if imp == 1:
        print ("Case #{}: IMPOSSIBLE".format(cnt))
    else:
        print ("Case #{}: {}".format(cnt, ans))
