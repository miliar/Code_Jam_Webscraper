__author__ = 'franyell'




def mymain():

    infile= open("in.txt")
    outfile=open("out.txt","w")
    cases = int(infile.readline().strip("\n"))+1

    for case in range(1,cases):
        s=infile.readline().strip('\n')
        min= getmin(s)
        createOutput(outfile,case,min)


    infile.close()
    outfile.close()

def createOutput(out,case,min):
    out.write("Case #"+str(case)+": "+str(min)+"\n")

def getmin(s):
    v=[ x for x in s.split()]
    smax=int(v[0])
    needs=0
    people=0
    lastZero=-1
    l=len(v[1])

    for x in range(0,l):
        inc=0
        if x>people:
            inc=x-people
            needs+=inc

        people+=inc+ int(v[1][x])
        if people>=smax:
            return needs
    return  needs






    return needs




mymain()