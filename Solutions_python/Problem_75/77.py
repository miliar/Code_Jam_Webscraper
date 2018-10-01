"""
Code Jam 2011 Qualification Round
Magicka by Warren Usui
"""
def pstack(data):
    rval = '['
    if len(data) == 0:
        return "[]"
    for i in data:
        rval += i+", "
    oval = rval[0:len(rval)-2]
    oval += ']'
    return oval

def magicka(fileHead):
    rootd = 'C:\\wutemp\\CodeJam\\2011'
    infile = "{0}\\{1}.in".format(rootd,fileHead)
    outfile = "{0}\\{1}.out".format(rootd,fileHead)
    fin = open(infile,'r')
    fout = open(outfile,'w')
    number = int(fin.readline())
    for iterv in xrange(0,number):
        txtin = fin.readline()
        parms = txtin.split(" ")
        indx = 0
        count1 = int(parms[indx])
        indx += 1
        cdict = {}
        for _ in xrange(0,count1):
            cdict[parms[indx][0:2]] = parms[indx][2]
            indx += 1
        count2 = int(parms[indx])
        indx += 1
        dlist = []
        for _ in xrange(0,count2):
            dlist.append(parms[indx])
            indx += 1
        count3 = int(parms[indx])
        teststr = parms[indx+1]
        stack = []
        for let in xrange(0,count3):
            stack.append(teststr[let])
            notdone = True
            while notdone:
                sz = len(stack)
                if sz < 2:
                    break
                else:
                    l1 = stack[sz-1]
                    l2 = stack[sz-2]
                    if l1+l2 in cdict:
                        stack.pop(sz-1)
                        stack.pop(sz-2)
                        stack.append(cdict[l1+l2])
                        continue
                    if l2+l1 in cdict:
                        stack.pop(sz-1)
                        stack.pop(sz-2)
                        stack.append(cdict[l2+l1])
                        continue
                    for elnum in xrange(0,sz-1):
                        tval = stack[elnum]
                        if tval+l1 in dlist:
                            stack = []
                            break
                        if l1+tval in dlist:
                            stack = []
                            break
                notdone = False
            indx += 1
        odata = "Case #{0}: {1}\n".format(iterv+1, pstack(stack))
        fout.write(odata)
        
if __name__ == '__main__':
    magicka('B-large')
