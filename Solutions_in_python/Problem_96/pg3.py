t = int(raw_input())
for i in xrange(t):
    a = raw_input()
    b = []
    b = a.split()
    b = map(int,b)
    n = b[0]
    s = b[1]
    p = b[2]
    b = b[3:]
    count = 0
    for x in b:
        flag = x % 3
        max1 = x / 3
        if flag == 1:
            max2 = max1
            max3 = max1 + 1
        if flag == 2:
            max2 = max1 + 1
            max3 = max1 + 1
        if flag == 0:
            max2 = max1
            max3 = max1
        if max3 >= p:
            count += 1
        else:
            if s != 0 and flag !=1 :
                max3 += 1
                max2 -= 1
                if max3 >=p and max2>=0 :
                    s -= 1
                    count += 1
    print "Case #%d: %d"%(i+1,count)
