import string

def getnxt(R,seq,cur):
    for i in range(cur+1,len(seq)):
        if seq[i][0] == R:
            return i
    return -1

ifile = open("input_large.txt")
fs = ifile.read().split("\n")
ifile.close()

T = int(fs[0])

out = []

NMidx = 1
for t in range(0,T):
    line = fs[NMidx].split(' ')
    N = int(line[0])
    bidx = 1
    #make them in array
    seq=[]
    for n in range(0,N):
        seq.append((line[n*2+1],int(line[n*2+2])))
        bidx+=2

    #one by one
    Opos = 1
    Bpos = 1
    Time = 0
    Oidx = getnxt('O',seq,-1)
    Bidx = getnxt('B',seq,-1)
    while True:
        if Oidx==-1 and Bidx==-1:
            break
        elif Oidx==-1:
            diff = abs(seq[Bidx][1]-Bpos)
            diff+=1
            if diff<=0:
                diff=1
            Time+=diff
            Bpos = seq[Bidx][1]
            Bidx = getnxt('B',seq,Bidx)
        elif Bidx==-1:
            diff = abs(seq[Oidx][1]-Opos)
            diff+=1
            if diff<=0:
                diff=1
            Time+=diff
            Opos = seq[Oidx][1]
            Oidx = getnxt('O',seq,Oidx)
        else:
            #get priority
            if Oidx<Bidx:
                diff = abs(seq[Oidx][1]-Opos)
                diff+=1
                Time += diff
                Opos = seq[Oidx][1]

                if diff>= abs(Bpos-seq[Bidx][1]):
                    Bpos = seq[Bidx][1]
                else:
                    if Bpos > seq[Bidx][1]:
                        Bpos -= diff
                        if Bpos < seq[Bidx][1]:
                            Bpos = seq[Bidx][1]
                    else:
                        Bpos += diff
                        if Bpos > seq[Bidx][1]:
                            Bpos = seq[Bidx][1]
                Oidx = getnxt('O',seq,Oidx)
            else:
                diff = abs(seq[Bidx][1]-Bpos)
                diff+=1
                Time += diff
                Bpos = seq[Bidx][1]


                if diff>= abs(Opos-seq[Oidx][1]):
                    Opos = seq[Oidx][1]
                else:
                    if Opos > seq[Oidx][1]:
                        Opos -= diff
                        if Opos < seq[Oidx][1]:
                            Opos = seq[Oidx][1]
                    else:
                        Opos += diff
                        if Opos > seq[Oidx][1]:
                            Opos = seq[Oidx][1]
                Bidx = getnxt('B',seq,Bidx)

    out.append("Case #"+str(t+1)+": %s\n"%str(Time))
    NMidx+=1

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()
