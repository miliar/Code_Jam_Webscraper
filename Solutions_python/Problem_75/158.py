def main():
    inpfile = open("B-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        linelst = inpfile.readline().strip().split()
        numcomb = int(linelst[0])
        linelst = linelst[1:]
        comb = linelst[:numcomb]
        linelst = linelst[numcomb:]
        numoppo = int(linelst[0])
        linelst = linelst[1:]
        oppo = linelst[:numoppo]
        linelst = linelst[numoppo:]
        numelem = int(linelst[0])
        linelst = linelst[1:]
        elem = linelst[0]
        #print comb
        #print oppo
        #print elem
        
        #print numcomb
        #print numoppo
        #print numelem
        resultlst = []
        length = len(elem)
        i = 0
        
        while i < length:
            #combine
            combined = False
            l = len(resultlst)
            if l > 0:
                curelem = elem[i]
                lastelem = resultlst[-1]
                for x in comb:
                    if (x[0] == curelem and x[1] == lastelem) or (x[1] == curelem and x[0] == lastelem):
                        resultlst[-1] = x[2]
                        combined = True
                        break
            #oppose
            opposed = False
            l = len(resultlst)
            if l > 0:
                if combined:
                    curelem = resultlst[-1]
                else:
                    curelem = elem[i]
                j = 0
                while j < l:
                    e = resultlst[j]
                    for x in oppo:
                        if (x[0] == curelem and x[1] == e) or (x[1] == curelem and x[0] == e):
                            resultlst = []
                            opposed = True
                            break
                    if opposed:
                        break
                    j += 1
            if (not opposed) and (not combined):    
                resultlst.append(elem[i])
            i += 1
            #print combined
            #print opposed
            #print resultlst
        #print resultlst
        temp = str(resultlst)
        out = ""
        for y in temp:
            if y != "\'":
                out += y
        result = "Case #" + str(case) + ": " + out + "\n"
        outfile.write(result)
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
