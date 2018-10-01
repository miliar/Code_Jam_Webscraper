import sys
import collections
import math


def solve(N):
    #print '====== ' + str(locals())
    if N <= 20:
        return N
    cnt = 0
    stop = False
    while (not stop):
        for i in xrange(N,0,-1):
            if i == 1:
                stop = True
            cnt += 1
            s = str(i)
            if  s[-1]=='1' and (
                (s[0] != '1' and len(s)==2) or 
                (2<len(s) and len(s)<=5 and s[-2]=='0') or
                (5<len(s) and len(s)<=8 and s[-2]=='0' and s[-3]=='0') or
                (8<len(s) and len(s)<=11 and s[-2]=='0' and s[-3]=='0' and s[-4]=='0') or
                (11<len(s) and len(s)<=14 and s[-2]=='0' and s[-3]=='0' and s[-4]=='0' and s[-5]=='0') or
                (14<len(s) and s[-2]=='0' and s[-3]=='0' and s[-4]=='0' and s[-5]=='0' and s[-6]=='0')
                ) and s > s[::-1]:
                #print i
                N = int('1' + (len(s)-1)*'0')
                cnt += int(s[::-1])-N
                break
    return cnt

if __name__ == '__main__':
    for case in range(int(raw_input())):
        print 'Case #%d: %d' % (case+1, solve(int(raw_input().strip())))