'''
Created on May 7, 2011

@author: jirasak
'''


if __name__ == '__main__':
    fIn = file('B-large.in')
    inLines = fIn.readlines()
    fIn.close()
    
    inLines = inLines[1:]
    numLines = len(inLines)
    i = 0
    xxx = 0
    while i < numLines:
        line = inLines[i].strip()
        elems = line.split(' ')
        numCombined = int(elems[0])
        cList = elems[1:numCombined+1]
        numOpposed = int(elems[1+numCombined])
        oList = elems[2+numCombined:numOpposed+2+numCombined]
        spellList = elems[3+numOpposed+numCombined]
        
        cList, oList, spellList
        resultList = []
        print 'Case #%d:' % (xxx+1), 
        xxx += 1
        for s in spellList:
            # Combine first
            combined = False
            if(len(resultList) >= 1):
                last = resultList[len(resultList)-1]
                for c in cList:
                    #print 'c', c[0:2], s, last
                    if (s == c[0] and last == c[1]) or (s == c[1] and last == c[0]):
                        #print 'popped', 
                        resultList.pop()
                        resultList.append(c[2])
                        #print 'debug',  resultList
                        combined = True
                        break
            if not combined:
                resultList.append(s)
            # Now clear the list...
            if(len(resultList) >= 1):
                last = resultList[len(resultList)-1]
                for o in oList:
                    if last in o:
                        thePair = None
                        x = o.find(last)
                        if x == 0:
                            thePair = o[1]
                        elif x == 1:
                            thePair = o[0]
                        else: # not found!
                            continue
                        if resultList.count(thePair) > 0:
                            resultList = []
                            break
            #print 'debugX', resultList
        print '[%s]' % (', '.join(resultList))
        
        i += 1
        #print line