def TidyNumbers():
    infile=open('B-small-attempt0.in')
    outfile=open('B-small-attempt0.out','w')
    T=int(infile.readline())
    tidy=1
    for x in range(T):
        N=int(infile.readline())
        for y in range(N,0,-1):
            s2=str(y)
            for z in range(1,len(s2)):
                if (int(s2[z])<int(s2[z-1])):
                    tidy=0
            if (tidy==1):
                break
            tidy=1
        s1='Case #'+str(x+1)+': '+s2+'\n'
        outfile.write(s1)
    infile.close()
    outfile.close()
    return

print(TidyNumbers())
