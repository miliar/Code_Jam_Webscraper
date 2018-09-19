import sys
import numpy as np

def read():
    return sys.stdin.readline()

def format(tup):
    return 'Case #%d: %s'%tup

def trs(num):
    snum = str(num)
    keta = len(str(num))
    tot = 0
    for i in xrange(keta):
        tot += int(snum[i])*int(snum[i])
    return tot

def kouho(keta):
    ary = []
    if keta%2 == 0:
        hketa = keta / 2
        end1 = '0' * (hketa -1) + '1'
        ary.append(end1[:-1] + '2') 
        ary.append(end1) 
        for i in xrange(hketa - 1):
            end2 = end1[:i]+ '1' + end1[i+1:]
            ary.append(end2)
            for j in xrange(i+1,hketa - 1):
                end3 = end2[:j]+ '1' + end2[j+1:]
                ary.append(end3)
                for k in xrange(j+1,hketa - 1):
                    end4 = end3[:k]+ '1' + end3[k+1:]
                    ary.append(end4)
        numary = [ int(a[::-1] + a) for a in ary]
    else:
        hketa = (keta + 1) / 2 
        end1 = '1' + '0'* (hketa - 2) + '1'
        end1a = '2' + '0' * (hketa - 2) + '1'
        end1b = '0'* (hketa - 1) + '1'
        ary.append('1' + '0'*(hketa - 2) + '2') 
        ary.append('0'*(hketa - 1) + '2') 
        ary.append('0'*(hketa - 1) + '1') 
        ary.append('2' + '0'*(hketa - 2) + '1') 
        ary.append('1' + '0'*(hketa - 2) + '1') 
        for i in xrange(1,hketa - 1):
            end2 = end1[:i]+ '1' + end1[i+1:]
            end2a = end1a[:i]+ '1' + end1a[i+1:]
            end2b = end1b[:i]+ '1' + end1b[i+1:]
            ary.append(end2)
            ary.append(end2a)
            ary.append(end2b)
            for j in xrange(i+1,hketa - 1):
                end3 = end2[:j]+ '1' + end2[j+1:]
                end3b = end2b[:j]+ '1' + end2b[j+1:]
                ary.append(end3)
                ary.append(end3b)
                for k in xrange(j+1,hketa - 1):
                    end4 = end3[:k]+ '1' + end3[k+1:]
                    end4b = end3b[:k]+ '1' + end3b[k+1:]
                    ary.append(end4)
                    ary.append(end4b)

        numary = [ int(a[::-1] + a[1:]) for a in ary]
    return sorted(numary)
ary = [1, 4, 9]
for i in xrange(2,52):
    for j in kouho(i):
        ary.append(j*j)
print len(str(ary[-1]))

ary = np.array(ary)
for i in xrange(int(read())):
    a, b = map(int,read().split()) 
    x = ary[a <= ary]
    y = x[x <= b]
    print format((i+1,len(y)))
