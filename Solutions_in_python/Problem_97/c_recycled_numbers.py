'''
Created on Apr 14, 2012

@author: jon
'''
import numpy as np
from qualround.FileReader import GoogleFileReader

def recycledNumbers(a, b):
    '''
    Constructor
    '''
    count = 0
    for n in range(a,b):
        ms = get_ms(n)
        count += ((ms > n) & (ms <= b)).sum()
#        for m in ms:
#            if m > n and m <= b:
#                count += 1
    return count

def get_ms(n):
    nstr = '{}'.format(n)
    ms = []
    for i in range(1,len(nstr)):
        ms.append(nstr[i:]+nstr[:i])
    return np.array(ms,dtype=int)


if __name__=="__main__":
    import sys; sys.argv=['','C-small-attempt0.in','C-small-attempt0.out']
    out = open(sys.argv[2],'w')
    fn = sys.argv[1]
    fr = GoogleFileReader(fn)
    for i, case in enumerate(fr):
        nums = np.array(case.split(),dtype=np.int32)
        count = recycledNumbers(nums[0], nums[1])
        output = "Case #{}: {}".format(i+1, count)
        print output
        out.write(output + '\n')
        