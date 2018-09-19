# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:46:34 2015

@author: 筱沫
"""

#data = []
#fr = open('a.txt')
#count = 1
#for line in fr.readlines()[1:]:
#
#    curLine = line.strip().split(' ')
#    data = map(int,curLine[1])
#    sumData = 0
#    result = 0
#    for i in range(len(data)):
#        if sumData >= i:
#            sumData = sumData + data[i]
#        else:
#            result = result + i - sumData
#            sumData = i + data[i]
#        
#    print 'Case #' + str(count)+': '+str(result)
##    print data
#    count = count + 1
#    data = []
#        
#fr.close()
#

count = 1
with open('b.txt') as f:
    lines = f.readlines()[2::2]
    for line in lines:
        numbers =  map(int,line.strip().split(' '))
        d, n = len(numbers), 0
        numbers.extend( [0]*1000 )
        maxnum = max(numbers)
        minute, add = maxnum, 0
        
        while( maxnum > 1):
            for i in range(d):
                if numbers[i] == maxnum:
                    numbers[i] = maxnum / 2
                    numbers[d+n] = maxnum - numbers[i]
                    n = n+1
                    add = add+1
            d = d+n
            maxnum = max(numbers)
            if maxnum + add <= minute:
                minute = maxnum + add
            else:
                break
        print "Case #"+ str(count) +": "+ str(minute)
        count = count + 1

#fr = open('b.txt')
#lines = fr.readlines()
#lines1 = lines[1::2]
#lines2 = lines[2::2]
#
#table = [['1','i','j','k'],
#         ['i','-1','k','-j'],
#         ['j','-k','-1','i'],
#         ['k','j','-i','-1']]
#def getCoord( x ):
#    coordi = {'1':0,'i':1,'j':2,'k':3}
#    return coordi[x]
#
#def multi(x, y):
#    if x[0] != '-' and y[0] != '-':
#        return table[getCoord(x)][getCoord(y)]
#    elif x[0] == '-' and y[0] == '-':
#        return multi(x[1:],y[1:])
#    else:
#        result = '-' + multi(x[-1],y[-1])
#        if result[1] == '-':
#            return result[2:]
#        else:
#            return result

#print reduce(multi,['j','k','i'])
#print reduce(multi,['k','i','j'])
#tmp = 'kk'*4464

#print reduce(multi, [x for x in tmp] )
#
#for i in range(len(lines1)) :
#
#    number = map(int,lines1[i].strip().split(' '))
#    ijk = lines2[i].strip()*number[-1]
#
#    result = reduce(multi, ijk)
#    if result != '-1':
#        print 'Case #' + str(i+1) +': NO'
#    elif not('j' in ijk or 'k' in ijk) or not('j' in ijk or 'i' in ijk) or not('i' in ijk or 'k' in ijk) :
#        print 'Case #' + str(i+1) +': NO'
#    else:
#        print 'Case #' + str(i+1) +': YES'
#
#fr.close()

#with open('d.txt','r') as f:
#    lines = f.readlines()[1:]
#    count = 1  
#    for line in lines:
#        x, r, c =  map(int, line.strip().split(' '))
#        if(x == 1 or x == 2) and (r*c)%2 == 0:
#            print "Case #"+str(count)+": GABRIEL"
#        elif (x == 1 or x == 3) and (r*c)%3 == 0 and (r>1 and c>1):
#            print "Case #"+str(count)+": GABRIEL"
#        elif (x == 1 or x == 4) and (r*c)%4 == 0 and r > 5 and c > 5:
#            print "Case #"+str(count)+": GABRIEL"
#        elif (r*c)%x or x==4 or x==3 and (r*c)%2==1:
#            print "Case #"+str(count)+": RICHARD"
#        else:
#            print "Case #"+str(count)+": RICHARD"
#        count = count + 1







