n = int(raw_input())

for x in range(1, n+1):
    data = raw_input().split()
    m = int(data[0])*2
    data = data[1:]

    po = [[]]
    pb = [[]]
    for y in range(0, m, 2):
        if data[y] == "O":
            po += [[data[y], int(data[y+1])]]
        else:
            pb += [[data[y], int(data[y+1])]]
    po += ["00"]
    pb += ["00"]
    
    tmp = [[]]
    for y in range(0, m, 2):
        tmp += [data[y] + data[y+1]]

    
    data = tmp
    m /= 2
    #print m
    #print po
    #print pb
    #print data
    t = 0
    o = 1
    so = 1
    b = 1
    sb = 1
    y = 1
    while y <= m:
        p = True
        #print ">>> ",
        #print data[y], po[so], pb[sb]
        if o < int(po[so][1]):
            o += 1
            #print "move O%d" %o
        elif o > int(po[so][1]):
            o -= 1
        else:
            tmp = po[so][0] + str(po[so][1])
            #print tmp, data[y]
            if tmp == data[y]:
                #print "push " + tmp
                so += 1
                y += 1
                p = False
                if y > m:
                    t += 1
                    break
            
        #print b < int(pb[sb][1])
        if b < int(pb[sb][1]):
            #print b, int(pb[sb][1])
            b += 1
            #print "move <B%d" %b
        elif b > int(pb[sb][1]):
            b -= 1
            #print "move >B%d" %b
        else:
            tmp = pb[sb][0] + str(pb[sb][1])
            #print tmp, data[y]
            if tmp == data[y] and p:
                #print "push " + tmp
                sb += 1
                y += 1
            
        t += 1
        
    print "Case #%d: %d" %(x, t)
