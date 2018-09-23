

outfile=open('outfileN_TO2017','w')

with open("B-small-attempt3.in") as fil:
    cases=int(fil.readline())
    out=""
    for case in xrange(cases):
        testline=fil.readline().split()
        N=int(testline[0]);
        liste=map(int,str(N))
        i=0
        result=N
        if len(liste)>1 and not all(liste[i] <= liste[i+1] for i in xrange(len(liste)-1)) :
            while(liste[i]<liste[i+1])and i< len(liste)-2: i+=1
            if i<len(liste):
                liste[i]-=1
                for i in xrange(i+1,len(liste)): liste[i]=9
            result= int(''.join(map(str, liste)))

        out+=("Case #%d: %s\n")%( case+1, result)
        
    
#print out
outfile.write(out)
outfile.close()
