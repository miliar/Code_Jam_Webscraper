'''
Created on Apr 13, 2013

@author: santosh
'''
import sys

if __name__ == '__main__':
    for t in xrange(int(raw_input())):
        (m,n)=[int(i) for i in raw_input().split()]
        ar=list()
        for i in xrange(m): ar.append([int(j) for j in raw_input().split()])
        flg=False
        for i in xrange(m):
            for j in xrange(n):
                if ar[i][j]==1:
                    if 2 in [ar[i][k] for k in xrange(n)] and 2 in [ar[k][j] for k in xrange(m)]: 
                        print 'Case #%d: NO'%(t+1)
                        flg=True
                if flg: break
            if flg : break
        if not flg: print 'Case #%d: YES'%(t+1)
            