import string

ifile = open("B-large.in")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    line = fs[NMidx].split(' ')
    C = int(line[0])
    COM = {}
    for i in range(1,C+1):
        COM[line[i][0:2]] = line[i][2]
        COM[line[i][1]+line[i][0]] = line[i][2]

    D = int(line[C+1])
    OPS = []
    for i in range(C+2,C+2+D):
        OPS.append(line[i])

    N = int(line[C+1+D+1])
    S = line[C+1+D+1+1]

    hand=[]
    for h in S:
        if hand==[]:
            hand.append(h)
            continue
        #test combine
        if COM.has_key(hand[-1]+h):
            hand[-1] = COM[hand[-1]+h]
            continue
        #test oppose
        is_ok = True
        for o in OPS:
            if o[0]==h:
                f = 1
            elif o[1]==h:
                f = 0
            else:
                continue
            if hand.count(o[f])>0:
                hand=[]
                is_ok = False
                break
        if is_ok:
            hand.append(h)


    out.append("Case #"+str(t+1)+": [%s]\n"%string.join(hand,', '))
    NMidx+=1

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()
