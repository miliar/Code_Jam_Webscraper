#RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
#WP (Winning Percentage) is the fraction of your games that you have won.
#OWP (Opponents' Winning Percentage) is the average WP of all your opponents
#OOWP (Opponents' Opponents' Winning Percentage) is the average OWP of all your opponents

def Wins(record):
    return record.count('1')

def Loses(record):
    return record.count('0')

def avg(L):
    return sum(L) / len(L)

def Sub(records):
    sub=[]
    for rec in records:
        sub.append(Wins(rec)/(Wins(rec)+Loses(rec)))
    return sum(rec)/len(rec)

def RPI(records):
    N=len(records)
    WP=[]
    OWP=[]
    OOWP=[]
    for r in range(N):
        record=records[r]
        WP.append(Wins(record)/(Wins(record)+Loses(record)))

        
        
        sub=[]
        for row in range(N):
            subrecord=records[row]
            if record[row]!='.':
                rec=subrecord[:r]+subrecord[r+1:]
                sub.append(Wins(rec)/(Wins(rec)+Loses(rec)))
        if len(sub)==0:continue
        OWP.append(sum(sub)/len(sub))

    for r in range(N):
        record=records[r]

        sOWP=[]
        for n in range(N):
            if record[n]!='.':
                #print(n,OWP)
                sOWP.append(OWP[n])
        OOWP.append(sum(sOWP)/len(sOWP))

    return (WP,OWP,OOWP)

infile=r'C:\Users\Jeff\Downloads\A-small-attempt1.in'
outfile=open(infile.replace('.in','.out'),'w')

lines=open(infile).read().split('\n')

Cases=int(lines.pop(0))
for case in range(Cases):
    N=int(lines.pop(0))
    records=[]
    for n in range(N):
        records.append(lines.pop(0).strip())
        
    out='Case #'+str(case+1)+':'
    print(out)
    outfile.write(out+'\n')

    WP,OWP,OOWP=RPI(records)
    
    for x in range(N):
        rpi = 0.25 * WP[x] + 0.50 * OWP[x] + 0.25 * OOWP[x]
        print('%.15f'%rpi)
        outfile.write('%.15f\n' % rpi)
        


outfile.close()
