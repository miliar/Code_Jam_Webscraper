# -*- coding: utf-8 -*-

ri = lambda: raw_input().strip()

num = int(ri())

rx = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
ox = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']

for i in xrange(num):
    data = []
    rdata = []
    all = []
    result = "Draw"
    
    for j in xrange(4):
        data.append(ri())
    
    for x in xrange(4):
        tmp = data[0][x]+data[1][x]+data[2][x]+data[3][x]
        all.append(tmp)
    
    for a in data:
        all.append(a)
    
    all.append(data[0][0]+data[1][1]+data[2][2]+data[3][3])
    all.append(data[0][3]+data[1][2]+data[2][1]+data[3][0])
    
   
    
    for x in all:
        if (x in rx) :
            result = "X won"
        elif x in ox:
            result = "O won"
        else:
            pass
    
    if result=="Draw":
        for a in all:
            for b in a:
                if b==".":
                    result = "Game has not completed"
                    break
    
    print "Case #{0}: {1}".format(i+1, result) 
    if i!=num-1:
        ri()