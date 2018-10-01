'''
Created on Aug 30, 2009

@author: jirasak
'''

import heapq

def proc_case(audlist):
    standing = 0
    i = 0
    friends = 0
    for numaud in audlist:
        if i <= standing:
            standing += numaud
        else:
            friends += i - standing
            standing += numaud + (i - standing)
        i += 1
    return friends

if __name__ == '__main__':
    afile = file('A-large.in')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline]
        maxnum = aline.split(' ')[0]
        audlist = [int(x) for x in aline.split(' ')[1]]
        cline += 1
        print 'Case #%d: %s' % (casenum, proc_case(audlist))