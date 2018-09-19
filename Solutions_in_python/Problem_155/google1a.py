'''
Created on 2013-9-23

@author: latifrons
'''
import sys

fin = None
fout = None

#debug_op = True
debug_op = False
debug = 2
    
def handle(case_no):
    l = fin.readline().strip()
    
    # input over
    if debug_op and case_no != debug:
        return
    
    (maxs, all ) = l.split(' ')
    maxs = int(maxs)
    i = 0
    sum = 0
    invite_sum = 0
    while i <= maxs:
        p = int(all[i])
        if sum < i and p != 0:
            # invite
            invite = i - sum
            invite_sum += invite
            sum += invite
        sum += p
        i += 1
    result = invite_sum
    return result
            

if __name__ == '__main__':
    #fin = sys.stdin
    fin = open('input.txt','r')
    
    fout = open('output.txt','w')
    cases = int(fin.readline())
    
    for i in range(cases):
        
        result = handle(i+1)
        s = 'Case #%d: %s'%(i+1,result)
        print s
        print >> fout, s
    
    fin.close()    
    fout.close()
    
    