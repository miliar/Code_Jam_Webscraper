def processcase(inlist):
    ans = "Broken"
    intlist =[]
    for i in inlist:
        intlist.append(int(i))
    if intlist[2] == 100:
        if intlist[1]<100:
            return "Broken"
    if intlist[2] == 0:
        if intlist[1]>0:
            return "Broken"
    if intlist[1] == 0:
        return "Possible"
    for j in range(1,intlist[0]+1):
        a = float(100)*float(j)/float(intlist[1])
        b = float(100)*float(j)//float(intlist[1])
        if a == b and a <= intlist[0]:
            return "Possible"
    return "Broken"


def inputfilter(filename):
    finput = open(filename,'r')
    fout = open("out.txt",'w')
    casenum = int(finput.readline())
    for i in range(1,casenum+1):
        inlist = finput.readline().split()
        print "Case #"+str(i)+": "+str(processcase(inlist))
        fout.write("Case #"+str(i)+": "+str(processcase(inlist))+'\n')
    finput.close()
    fout.close()

    
if __name__=="__main__":
    inputfilter("A-small-attempt1.in")