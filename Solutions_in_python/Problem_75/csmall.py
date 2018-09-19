from string import *

def solve(file):

    f = open("out_"+file,'w')
    inp = open(file)    
    n = int(inp.readline())


    for c in range(n):
        comb = {}
        opp = []
        resp = ""
        line = inp.readline()
        sline = split(line)
        nc = int(sline[0])
        for i in range(nc):
            comb[sline[i + 1][0:2]] = sline[i+1][2]
            comb[sline[i + 1][1] + sline[i + 1][0]] = sline[i+1][2]

        no = int(sline[nc + 1])
        for j in range(no):
            opp.append(sline[j + nc + 2])
            opp.append(sline[j + nc + 2][1]+sline[j + nc + 2][0])

        strg = sline[nc + no + 3]
        
        for x in range(len(strg)):
            resp += strg[x]
            l = len(resp)
            if l>1:
                if comb.has_key(resp[l-2:]):
                    resp = resp[:l-2] + comb[resp[l-2:]]
                
                l = len(resp)

                for i in range(l-1):
                    if opp.count(resp[i]+resp[l-1]):
                        resp = ""
                        break

        sresp = "Case #"+str(c+1)+": ["
        
        for x in range(len(resp)):
            sresp += resp[x] + ", "

        if len(resp)>0:
            sresp = sresp[:len(sresp)-2] + ']\n'
        else:
            sresp += ']\n'


        f.write(sresp)            
        print sresp
                            
        
