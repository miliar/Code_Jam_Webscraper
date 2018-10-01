'''
Jirasak Chirathivat
'''

import os
import os.path
import sys
sys.setrecursionlimit(1000000000)

#### CHANGE HERE ####
filename = 'c.test'
#### CHANGE HERE ####


def solve(inword, tofind):
    count = 0
    # check resultTable
    # if inword
    if globals()['res'].has_key((inword, tofind)):
        return globals()['res'][(inword, tofind)]
    
    for i in range(len(inword)):
        char = inword[i]
        if char == tofind[0]:
            if len(tofind) == 1:
                count += 1
            else:
                count += solve(inword[i + 1:], tofind[1:])
    
    globals()['res'][(inword, tofind)] = count
    
    return count


def process(casenum, casedata):
    #### CHANGE HERE ####
    inword, tofind = casedata
    resultTable = {}
    globals()['res'] = resultTable
    return solve(inword, tofind)
    #### CHANGE HERE ####

if __name__ == '__main__':
    afile = file(filename)
    aread = afile.readlines()
    afile.close()
    
    out = file('cout.txt', 'w')
    casefile = file('casefile.txt', 'w')
    
    aread = [x.strip() for x in aread]
    
    numcase = int(aread[0])
    
    line = 1
    for i in range(1, numcase + 1):
        
        #### CHANGE HERE ####
        pattern = aread[line]
        #### CHANGE HERE ####
        
        #### CHANGE HERE ####
        caseData = (pattern, 'welcome to code jam')
        tomove = 1
        #### CHANGE HERE ####

        if False:
            print >> casefile, 'Case #%s' % i
            print >> casefile, '%s\n' % '\n'.join(aread[line: line + tomove])
            print >> casefile, '%s\n\n\n' % ('\n'.join([str(x) for x in caseData]))
        
        #### CHANGE HERE ####
        line += tomove
        #### CHANGE HERE
        
        print >> out, 'Case #%s: %.4d' % (i, process(i, caseData) % 1000)
    
    casefile.close()
    out.close()
    #os.startfile('out.txt')
    #os.startfile('casefile.txt')  
