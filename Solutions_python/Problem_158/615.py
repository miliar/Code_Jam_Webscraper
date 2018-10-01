'''
Created on Aug 30, 2009

@author: jirasak
'''

import heapq
import math

mapping = '''1    1    YES    NO    NO    NO
1    2    YES    YES    NO    NO
1    3    YES    NO    NO    NO
1    4    YES    YES    NO    NO
2    2    YES    YES    NO    NO
2    3    YES    YES    YES    NO
2    4    YES    YES    NO    NO
3    3    YES    NO    YES    NO
4    3    YES    YES    YES    YES
4    4    YES    YES    NO    YES'''.splitlines()


def proc_case(x, r, c, data_mapping):
    return 'GABRIEL' if data_mapping[(x, r, c)] == 'YES' else 'RICHARD'

if __name__ == '__main__':
    data_mapping = {}
    for m in mapping:
        r, c = m.split('    ')[0:2]
        results = m.split('    ')[2:]
        for x in range(1, 5):
            data_mapping[(str(x), r, c)] = results[x-1]
            data_mapping[(str(x), c, r)] = results[x-1]

#     print sorted(data_mapping.keys())

    afile = file('D-small-attempt2.in')
    aread = afile.readlines()
    afile.close()
    
    aread = [x.strip() for x in aread]
    numcase = int(aread[0])
    
    cline = 1
    for casenum in range(1, numcase + 1):
        aline = aread[cline]
        x, r, c = [x for x in aread[cline].split(' ')]
        data = aline
        cline += 1
        outputline = 'Case #%d: %s' % (casenum, proc_case(x, r, c, data_mapping))
        print outputline