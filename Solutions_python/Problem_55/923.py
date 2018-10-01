'''
Created on May 8, 2010

@author: Gary
'''

import sys

if __name__ == '__main__':
    file = open(sys.argv[1])
    out = open('output.out','w')
    sys.stdout = out
    n = int(file.readline())
    for i in range(n):
        li1 = map(int,file.readline().split())
        R, k, N = li1
        queue = map(int,file.readline().split())
        total = sum(queue)
        if total <= k:
            print "Case #%d: %d" % (i+1,total*R)
        else:
            rev, rep, load, j = 0,0,0,0
            while rep<R:
                if load+queue[j] > k:
                    rev += load
                    load = 0
                    rep += 1
                load += queue[j]
                j = (j+1)%len(queue)
                
            print "Case #%d: %d" % (i+1,rev)
        
