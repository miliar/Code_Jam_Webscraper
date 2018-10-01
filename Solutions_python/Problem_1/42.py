import math

def solve(fstr):
    outStr = ""
    ipt = fstr.strip().split('\n')
    ipt = ipt[1:]
    data = [] #list of (engines, queries)
    iptInd = 0
    while (iptInd < len(ipt)):
        nOfSEs = int(ipt[iptInd])
        ind = iptInd + nOfSEs + 1
        nOfQrs = int(ipt[ind])
        data.append((ipt[iptInd+1:ind], ipt[ind+1:ind+nOfQrs+1]))
        iptInd = ind + nOfQrs + 1
    
    print str(data)

    for tcInd in range(len(data)):
        tc = data[tcInd]
        ses = []
        ses.extend(tc[0])
        qrs = tc[1]
        swt = 0
        for qr in qrs:
            if (len(ses) > 1):
                if (ses.count(qr) > 0):
                    ses.remove(qr)
                continue
            if (ses[0] == qr):
                ses = []
                ses.extend(tc[0])
                ses.remove(qr)
                swt += 1
            
        outStr += "Case #" + str(tcInd+1) +": " + str(swt) + "\n"

    return outStr
    

ipt = None
opt = None
try:
    prog = "A"
    fName = "A-large.in"
    iptF = file("e:\GCJ\\" + prog + "\\" + fName)
    outStr = solve(iptF.read())
    print outStr
    optF = file("e:\GCJ\\" + prog + "\output.txt",'w+')
    optF.write(outStr)
    optF.close()
    if (fName == "input.txt"):    
        otstF = file("e:\GCJ\\" + prog + "\outtest.txt")
        otst = otstF.read()
        otstF.close()
        if (otst == outStr):
            print "+++++++++++++++ CORRETO +++++++++++++++++"
        else:
            print "______________ INCORRETO ________________"
finally:
    if (iptF != None):
        iptF.close()
