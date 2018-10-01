#!/usr/bin/env python
#coding=utf-8

def PrintCase(caseNo, result):
    tmp = "Case #" + str(caseNo) + ": " + str(result)
    return tmp

def main():
    mapOfRule = {'z':'q'}
    allChar = 'abcdefghijklmnopqrstyvwxyz \n'
    
    keySet = set()
    valueSet = set()
    for tmpChar in allChar:
        keySet.add(tmpChar)
        valueSet.add(tmpChar)
        
    questionLines = ['ejp mysljylc kd kxveddknmc re jsicpdrysi\n',
                     'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\n',
                       'de kr kd eoya kw aej tysr re ujdr lkgc jv\n']
    answerLines = ['our language is impossible to understand\n',
                   'there are twenty six factorial possibilities\n',
                   'so it is okay if you want to just give up\n']
    for i in range(0, 3):
        j = 0
        for tmpChar in questionLines[i] :
            mapOfRule[tmpChar] = answerLines[i][j]
            if tmpChar in keySet:
                keySet.remove(tmpChar)
            if answerLines[i][j] in valueSet:
                valueSet.remove(answerLines[i][j])
            j += 1
    
    keySet.remove('z')
    valueSet.remove('q')
    
    if len(keySet) == 1 and len(valueSet) == 1:
        mapOfRule[list(keySet)[0]] = list(valueSet)[0]
    
    for k,v in mapOfRule.items():
        print k + '->' + v
    
    file = open("A-small-attempt2.in", 'r')
    i = 0
    resStr = ''
    for tmpContext in file.readlines():
        if i == 0 :
            i += 1
            continue
        tmpResStr = ""
        for tmpChar in tmpContext:
            tmpResStr += mapOfRule[tmpChar]
            
        resStr += PrintCase(i, tmpResStr)
        i += 1
    
    print resStr
    
    resultFile = open('a.out', 'w')
    resultFile.write(resStr)
    resultFile.close()
    file.close()
    
if __name__ == '__main__':
    main()

